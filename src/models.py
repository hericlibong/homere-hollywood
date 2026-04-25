from typing import Literal
from pydantic import BaseModel

SourcePrincipale = Literal[
    "L'Iliade",
    "Le Cycle Troyen",
    "Héritage Gréco-Romain",
    "Adaptation Cinéma",
]


class InputScene(BaseModel):
    scene_number: int
    scene_heading: str | None
    characters: list[str]
    dialogue_count: int
    action_count: int
    full_text: str


class OutputScene(BaseModel):
    scene_number: int
    scene_heading: str | None
    characters: list[str]
    action_film: str
    source_principale: SourcePrincipale
    reference_iliade: str
    explication_litteraire: str
