import json
from pathlib import Path


def load_text_config(path):
    path_obj = Path(path)
    if not path_obj.exists():
        return {"error": f"Config file not found: {path}"}
    return {
        "path": str(path_obj),
        "suffix": path_obj.suffix,
        "message": "Placeholder loader only; YAML parsing not enabled in this prototype."
    }


def load_dataset_registry():
    return {
        "datasets": [
            "HC3",
            "GenImage",
            "DFDC",
            "FaceForensics++",
            "Celeb-DF",
            "FakeAVCeleb"
        ]
    }


if __name__ == "__main__":
    print(json.dumps(load_dataset_registry(), ensure_ascii=False, indent=2))
"""
Configuration loader for repository-adapted dataset settings.

The original document refers to datasets_config.json.
This repository stores the configuration in YAML format for readability.
"""
