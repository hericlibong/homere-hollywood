"""
Test comparatif : analyse 5 scènes avec Sonnet 4.6 ET Opus 4.7,
puis génère output/comparison_results.json avec les réponses et métriques côte-à-côte.
"""
import json
import logging
from copy import deepcopy
from pathlib import Path

from src.client import AnthropicClient
from src.config import load_config
from src.loader import load_scenes, load_system_prompt
from src.logger import setup_logger
from src.validator import validate

MODELS = {
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
}


def run_comparison(config_path: str = "config.yaml"):
    config = load_config(config_path)
    logger = setup_logger(config.log_path)
    logger.info("Démarrage test comparatif Sonnet vs Opus")

    system_prompt = load_system_prompt(config.system_prompt_path)
    all_scenes = load_scenes(config.input_path)
    target_indices = config.comparison_scenes
    scenes = [s for s in all_scenes if s.scene_number in target_indices]

    results = []

    for scene in scenes:
        entry: dict = {"scene_number": scene.scene_number, "scene_heading": scene.scene_heading}
        total_cost = 0.0

        for label, model_id in MODELS.items():
            cfg = deepcopy(config)
            cfg.model = model_id
            client = AnthropicClient(cfg)

            try:
                api_result = client.analyze_scene(scene, system_prompt)
                is_valid, data, error = validate(api_result.content)
                entry[label] = {
                    "model": model_id,
                    "valid": is_valid,
                    "result": data if is_valid else None,
                    "raw": api_result.content if not is_valid else None,
                    "validation_error": error,
                    "tokens_in": api_result.input_tokens,
                    "tokens_out": api_result.output_tokens,
                    "cost_usd": round(api_result.cost_usd, 5),
                }
                total_cost += api_result.cost_usd
                logger.info(
                    f"Comparaison scene={scene.scene_number} {label} | "
                    f"valid={is_valid} cost=${api_result.cost_usd:.5f}"
                )
            except Exception as exc:
                logger.error(f"Comparaison scene={scene.scene_number} {label} | ERREUR : {exc}")
                entry[label] = {"model": model_id, "error": str(exc)}

        entry["total_cost_usd"] = round(total_cost, 5)
        results.append(entry)

    output_path = Path("output/comparison_results.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    grand_total = sum(r.get("total_cost_usd", 0) for r in results)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(
            {"scenes_compared": len(results), "grand_total_cost_usd": round(grand_total, 5), "results": results},
            f,
            ensure_ascii=False,
            indent=2,
        )

    logger.info(f"Comparaison terminée | coût total=${grand_total:.5f} | fichier={output_path}")
    print(f"\nRésultats sauvegardés dans {output_path}")
    print(f"Coût total du test comparatif : ${grand_total:.4f}")


if __name__ == "__main__":
    run_comparison()
