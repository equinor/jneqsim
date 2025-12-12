from pathlib import Path

import yaml


def load_config(config_path: Path) -> dict:
    """Load configuration from YAML file"""
    with open(config_path) as f:
        return yaml.safe_load(f)
