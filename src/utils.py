import logging
import yaml
from typing import Any, Dict


def setup_logging(log_file: str = 'project.log') -> None:
    """
    Set up logging configuration.
    """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s'
    )


def load_config(config_path: str) -> Dict[str, Any]:
    """
    Load a YAML configuration file.
    """
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config 