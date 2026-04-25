import json
import logging
import time
from pathlib import Path

from src.checkpoint import Checkpoint
from src.client import AnthropicClient
from src.config import Config
from src.loader import load_scenes, load_system_prompt
from src.validator import build_retry_feedback, validate


def run(config: Config, scenes_filter: list[int] | None = None, limit: int | None = None):
    logger = logging.getLogger("troy_pipeline")
    system_prompt = load_system_prompt(config.system_prompt_path)
    scenes = load_scenes(config.input_path)
    checkpoint = Checkpoint(config.progress_path)
    client = AnthropicClient(config)

    if scenes_filter:
        scenes = [s for s in scenes if s.scene_number in scenes_filter]
    if limit:
        scenes = scenes[:limit]

    total = len(scenes)
    logger.info(f"Démarrage pipeline | modèle={config.model} | scènes à traiter={total}")

    for idx, scene in enumerate(scenes, 1):
        if checkpoint.is_processed(scene.scene_number):
            logger.info(f"scene={scene.scene_number} | SKIP (déjà traitée)")
            continue

        logger.info(f"scene={scene.scene_number} | {idx}/{total} | traitement en cours")
        t0 = time.monotonic()

        feedback = None
        success = False

        for attempt in range(1, config.max_retries + 2):  # 1 essai initial + max_retries
            try:
                result = client.analyze_scene(scene, system_prompt, retry_feedback=feedback)
            except Exception as exc:
                logger.error(f"scene={scene.scene_number} | ERREUR API : {exc}")
                checkpoint.mark_failed(scene.scene_number, str(exc))
                break

            is_valid, data, error = validate(result.content)

            if is_valid:
                elapsed = round(time.monotonic() - t0, 2)
                checkpoint.mark_processed(
                    scene.scene_number,
                    result=data,
                    tokens_in=result.input_tokens,
                    tokens_out=result.output_tokens,
                    cost=result.cost_usd,
                )
                logger.info(
                    f"scene={scene.scene_number} | OK | "
                    f"tokens_in={result.input_tokens} tokens_out={result.output_tokens} "
                    f"cost=${result.cost_usd:.4f} duration={elapsed}s"
                )
                success = True
                break
            else:
                logger.warning(
                    f"scene={scene.scene_number} | validation échouée (tentative {attempt}) : {error}"
                )
                if attempt <= config.max_retries:
                    feedback = build_retry_feedback(error)
                else:
                    _save_raw_failure(config.failed_raw_dir, scene.scene_number, result.content)
                    checkpoint.mark_failed(scene.scene_number, error)
                    logger.error(
                        f"scene={scene.scene_number} | ÉCHEC après {config.max_retries + 1} tentatives"
                    )

        _ = success  # noqa: F841

    _write_output(config.output_path, checkpoint)
    summary = checkpoint.summary()
    logger.info(
        f"Pipeline terminé | traités={summary['processed']} échoués={summary['failed']} "
        f"coût_total=${summary['total_cost_usd']} "
        f"tokens_in={summary['total_tokens_in']} tokens_out={summary['total_tokens_out']}"
    )
    return summary


def _save_raw_failure(failed_dir: Path, scene_number: int, raw: str):
    failed_dir.mkdir(parents=True, exist_ok=True)
    (failed_dir / f"scene_{scene_number}.txt").write_text(raw, encoding="utf-8")


def _write_output(output_path: Path, checkpoint: Checkpoint):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    results = checkpoint.get_all_results()
    results.sort(key=lambda r: r["scene_number"])
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump({"total_scenes": len(results), "scenes": results}, f, ensure_ascii=False, indent=2)
