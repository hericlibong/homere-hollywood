import json
import re
from typing import Any

from pydantic import ValidationError

from src.models import OutputScene

_JSON_BLOCK_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)


def validate(raw: str) -> tuple[bool, dict[str, Any] | None, str | None]:
    parsed = _parse_json(raw)
    if parsed is None:
        return False, None, f"Impossible de parser le JSON depuis la réponse : {raw[:200]}"

    try:
        OutputScene.model_validate(parsed)
        return True, parsed, None
    except ValidationError as exc:
        return False, None, str(exc)


def _parse_json(text: str) -> dict | None:
    text = text.strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    match = _JSON_BLOCK_RE.search(text)
    if match:
        try:
            return json.loads(match.group(1))
        except json.JSONDecodeError:
            pass

    return None


def build_retry_feedback(error: str) -> str:
    schema = {
        "scene_number": "int",
        "scene_heading": "str | null",
        "characters": ["str"],
        "action_film": "str",
        "source_principale": "L'Iliade | Le Cycle Troyen | Héritage Gréco-Romain | Adaptation Cinéma",
        "reference_iliade": "str",
        "explication_litteraire": "str",
    }
    return (
        f"Ta réponse précédente a échoué la validation JSON avec l'erreur suivante :\n{error}\n\n"
        f"Retourne UNIQUEMENT un objet JSON valide (sans balise markdown) respectant ce schéma :\n"
        f"{json.dumps(schema, ensure_ascii=False, indent=2)}"
    )
