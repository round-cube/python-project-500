import os
import json
import yaml
from pathlib import Path


def get_dict_from_file(path_file):
    file_ext = Path(path_file).suffix
    return open_file(path_file, file_ext)


def open_file(path_file, file_ext):
    path_file = os.path.basename(path_file)
    with open(Path() / 'tests/fixtures' / path_file) as f:
        if file_ext.lower() == '.json':
            return json.load(f)
        elif file_ext.lower() == '.yml' or file_ext.lower() == '.yaml':
            return yaml.safe_load(f)
