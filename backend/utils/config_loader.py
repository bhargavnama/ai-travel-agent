import yaml
from pathlib import Path

def load_config(config_path: str = None) -> dict:
    if config_path is None:
        config_path = Path(__file__).resolve().parent.parent / "config" / "config.yaml"

    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
        print(config)

    return config