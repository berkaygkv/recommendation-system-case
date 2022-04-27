from pathlib import Path
import os
from src.data.config_reader import *

def get_path(*args):
    """Returns the path of the desired file
    """
    ROOT_STRING = get_root_dir()
    raw_data_path = Path(ROOT_STRING, *args)
    return raw_data_path

def get_root_dir():
    """Returns project root path
    """
    configs = load_config()
    ROOT_NAME = configs["ROOT"]
    ROOT_STRING = os.getcwd().split(ROOT_NAME)[0] + ROOT_NAME
    ROOT_DIR = Path(ROOT_STRING)
    return ROOT_DIR