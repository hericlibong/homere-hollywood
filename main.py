"""
Point d'entrée du pipeline d'analyse littéraire — Troy (227 scènes).

Usage :
  python main.py                          # run complet avec le modèle de config.yaml
  python main.py --model opus             # forcer Opus 4.7
  python main.py --limit 10              # traiter seulement les 10 premières scènes
  python main.py --scenes 0,50,100       # scènes spécifiques
  python main.py --compare               # test comparatif Sonnet vs Opus
  python main.py --reset                 # effacer le checkpoint (confirmation requise)
"""
import argparse
import sys

from src.config import load_config
from src.logger import setup_logger

MODELS_MAP = {
    "sonnet": "claude-sonnet-4-6",
    "opus": "claude-opus-4-7",
}


def main():
    parser = argparse.ArgumentParser(description="Pipeline d'analyse littéraire — Troy")
    parser.add_argument("--model", choices=["sonnet", "opus"], help="Modèle à utiliser")
    parser.add_argument("--limit", type=int, metavar="N", help="Traiter seulement les N premières scènes")
    parser.add_argument(
        "--scenes",
        metavar="N,N,...",
        help="Numéros de scènes spécifiques (séparés par des virgules)",
    )
    parser.add_argument("--compare", action="store_true", help="Lancer le test comparatif Sonnet vs Opus")
    parser.add_argument("--reset", action="store_true", help="Effacer le checkpoint et repartir de zéro")
    parser.add_argument("--config", default="config.yaml", help="Chemin du fichier de configuration")
    args = parser.parse_args()

    config = load_config(args.config)
    logger = setup_logger(config.log_path)

    if args.model:
        config.model = MODELS_MAP[args.model]
        logger.info(f"Modèle forcé via CLI : {config.model}")

    if args.reset:
        confirm = input(
            f"Êtes-vous sûr de vouloir effacer le checkpoint ({config.progress_path}) ? [oui/non] : "
        )
        if confirm.strip().lower() != "oui":
            print("Annulé.")
            sys.exit(0)
        from src.checkpoint import Checkpoint
        Checkpoint(config.progress_path).reset()
        logger.info("Checkpoint effacé.")
        print("Checkpoint effacé. Relancez sans --reset pour repartir de zéro.")
        sys.exit(0)

    if args.compare:
        from compare import run_comparison
        run_comparison(args.config)
        sys.exit(0)

    scenes_filter = None
    if args.scenes:
        try:
            scenes_filter = [int(n.strip()) for n in args.scenes.split(",")]
        except ValueError:
            parser.error("--scenes doit contenir des entiers séparés par des virgules (ex: 0,50,100)")

    from src.pipeline import run
    summary = run(config, scenes_filter=scenes_filter, limit=args.limit)

    print(
        f"\n{'='*50}\n"
        f"Pipeline terminé\n"
        f"  Traitées  : {summary['processed']}\n"
        f"  Échouées  : {summary['failed']}\n"
        f"  Coût total: ${summary['total_cost_usd']}\n"
        f"  Sortie    : {config.output_path}\n"
        f"{'='*50}"
    )


if __name__ == "__main__":
    main()
