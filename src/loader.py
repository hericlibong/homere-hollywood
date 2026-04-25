import json
from pathlib import Path

from src.models import InputScene


def load_scenes(input_path: Path) -> list[InputScene]:
    with open(input_path, encoding="utf-8") as f:
        data = json.load(f)
    return [InputScene(**scene) for scene in data["scenes"]]


def load_system_prompt(prompt_path: Path) -> str:
    text = prompt_path.read_text(encoding="utf-8").strip()
    if text.startswith("# PLACEHOLDER"):
        raise ValueError(
            f"Le prompt système n'a pas été configuré : {prompt_path}\n"
            "Remplacez le contenu de ce fichier par votre prompt calibré."
        )
    return text
