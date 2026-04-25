import time
from dataclasses import dataclass

import anthropic

from src.config import Config
from src.models import InputScene

# Pricing USD per million tokens — source : platform.claude.com/docs/en/docs/about-claude/models
# Cache : write = 125% input, read = 10% input (politique standard Anthropic)
_PRICING = {
    "claude-sonnet-4-6": {"input": 3.0, "output": 15.0, "cache_write": 3.75, "cache_read": 0.30},
    "claude-opus-4-7":   {"input": 5.0, "output": 25.0, "cache_write": 6.25, "cache_read": 0.50},
}

# Opus 4.7 utilise adaptive thinking — temperature n'est pas supporté
_NO_TEMPERATURE_MODELS = {"claude-opus-4-7"}


@dataclass
class ApiResult:
    content: str
    input_tokens: int
    output_tokens: int
    cache_creation_tokens: int
    cache_read_tokens: int
    cost_usd: float


class AnthropicClient:
    def __init__(self, config: Config):
        self.config = config
        self._client = anthropic.Anthropic(api_key=config.api_key)
        self._pricing = _PRICING.get(config.model, _PRICING["claude-sonnet-4-6"])

    def analyze_scene(
        self,
        scene: InputScene,
        system_prompt: str,
        retry_feedback: str | None = None,
    ) -> ApiResult:
        user_content = self._build_user_message(scene)
        if retry_feedback:
            user_content = f"{user_content}\n\n---\n{retry_feedback}"

        kwargs: dict = {
            "model": self.config.model,
            "max_tokens": 1024,
            "system": [
                {
                    "type": "text",
                    "text": system_prompt,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            "messages": [{"role": "user", "content": user_content}],
        }
        if self.config.model not in _NO_TEMPERATURE_MODELS:
            kwargs["temperature"] = self.config.temperature

        for attempt in range(4):  # 1 essai + 3 backoffs
            try:
                response = self._client.messages.create(**kwargs)
                return self._parse_response(response)
            except anthropic.RateLimitError:
                time.sleep(min(2 ** attempt * 2, 60))
            except anthropic.APIStatusError as exc:
                if exc.status_code >= 500 and attempt < 3:
                    time.sleep(min(2 ** attempt * 2, 60))
                else:
                    raise

        raise RuntimeError(f"Échec de l'appel API après plusieurs tentatives pour la scène {scene.scene_number}")

    def _build_user_message(self, scene: InputScene) -> str:
        characters = ", ".join(scene.characters) if scene.characters else "Aucun personnage listé"
        heading = scene.scene_heading or "Non spécifié"
        return (
            f"Scène numéro : {scene.scene_number}\n"
            f"Indication scénique : {heading}\n"
            f"Personnages : {characters}\n"
            f"Répliques : {scene.dialogue_count} | Actions : {scene.action_count}\n\n"
            f"Texte complet :\n{scene.full_text}"
        )

    def _parse_response(self, response) -> ApiResult:
        usage = response.usage
        input_tokens = usage.input_tokens
        output_tokens = usage.output_tokens
        cache_creation = getattr(usage, "cache_creation_input_tokens", 0) or 0
        cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0

        p = self._pricing
        cost = (
            (input_tokens / 1_000_000) * p["input"]
            + (output_tokens / 1_000_000) * p["output"]
            + (cache_creation / 1_000_000) * p["cache_write"]
            + (cache_read / 1_000_000) * p["cache_read"]
        )

        content = response.content[0].text if response.content else ""
        return ApiResult(
            content=content,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cache_creation_tokens=cache_creation,
            cache_read_tokens=cache_read,
            cost_usd=cost,
        )
