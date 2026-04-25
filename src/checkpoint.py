import json
import os
from pathlib import Path
from typing import Any


class Checkpoint:
    def __init__(self, path: Path):
        self.path = path
        self._data: dict[str, Any] = self._load()

    def _load(self) -> dict[str, Any]:
        if self.path.exists():
            with open(self.path, encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(self._data, f, ensure_ascii=False, indent=2)
        os.replace(tmp, self.path)

    def is_processed(self, scene_number: int) -> bool:
        entry = self._data.get(str(scene_number))
        return entry is not None and entry.get("status") == "processed"

    def is_failed(self, scene_number: int) -> bool:
        entry = self._data.get(str(scene_number))
        return entry is not None and entry.get("status") == "failed"

    def mark_processed(self, scene_number: int, result: dict, tokens_in: int, tokens_out: int, cost: float):
        self._data[str(scene_number)] = {
            "status": "processed",
            "result": result,
            "tokens_in": tokens_in,
            "tokens_out": tokens_out,
            "cost": cost,
        }
        self._save()

    def mark_failed(self, scene_number: int, error: str):
        self._data[str(scene_number)] = {
            "status": "failed",
            "error": error,
        }
        self._save()

    def get_all_results(self) -> list[dict]:
        return [
            entry["result"]
            for entry in self._data.values()
            if entry.get("status") == "processed"
        ]

    def summary(self) -> dict:
        processed = sum(1 for e in self._data.values() if e.get("status") == "processed")
        failed = sum(1 for e in self._data.values() if e.get("status") == "failed")
        total_cost = sum(
            e.get("cost", 0.0) for e in self._data.values() if e.get("status") == "processed"
        )
        total_tokens_in = sum(
            e.get("tokens_in", 0) for e in self._data.values() if e.get("status") == "processed"
        )
        total_tokens_out = sum(
            e.get("tokens_out", 0) for e in self._data.values() if e.get("status") == "processed"
        )
        return {
            "processed": processed,
            "failed": failed,
            "total_cost_usd": round(total_cost, 4),
            "total_tokens_in": total_tokens_in,
            "total_tokens_out": total_tokens_out,
        }

    def reset(self):
        self._data = {}
        self._save()
