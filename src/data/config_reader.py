import yaml
from pathlib import Path
from src.data.path_finder import get_root_dir

def load_config():
    """Loads config file
    """

    # Find the root directory of the project and read config file
    ROOT_DIR = get_root_dir()
    config_file_path = Path(ROOT_DIR, "config.yaml")
    with open(config_file_path, "r") as f:
        configs = yaml.safe_load(f)
    return configs
