import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    model: str
    max_retries: int
    temperature: float
    input_path: Path
    output_path: Path
    progress_path: Path
    failed_raw_dir: Path
    system_prompt_path: Path
    log_path: Path
    comparison_scenes: list[int]
    api_key: str = field(default_factory=lambda: os.environ["ANTHROPIC_API_KEY"])

    def __post_init__(self):
        self.input_path = Path(self.input_path)
        self.output_path = Path(self.output_path)
        self.progress_path = Path(self.progress_path)
        self.failed_raw_dir = Path(self.failed_raw_dir)
        self.system_prompt_path = Path(self.system_prompt_path)
        self.log_path = Path(self.log_path)


def load_config(config_path: str = "config.yaml") -> Config:
    with open(config_path) as f:
        data = yaml.safe_load(f)
    return Config(**data)
