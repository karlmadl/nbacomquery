import yaml
from pathlib import Path


def load_yaml(
    file: Path,
) -> dict:  # add exception handling for loading unknown .yaml files
    try:
        with open(file) as f:
            return yaml.full_load(f)
    except FileNotFoundError:
        raise ValueError(f"{file.stem} is not a valid stats_type")


def build_yaml_path(file: str) -> Path:
    return Path(__file__).parent.joinpath(f"config/{file}")
