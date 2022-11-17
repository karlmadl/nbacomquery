import yaml
from pathlib import Path


def load_yaml(file: str) -> dict:
    with open(file) as f:
        return yaml.full_load(f)


def build_yaml_path(file: str) -> str:
    return Path(__file__).parent.joinpath(f"config/{file}")
