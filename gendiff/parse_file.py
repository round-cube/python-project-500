import os
import json
import yaml
from pathlib import Path


def get_dict_from_file(path_file):
    file_ext = Path(path_file).suffix
    path_file = Path() / 'tests/fixtures' / os.path.basename(path_file)
    f = open(path_file)
    return open_file(f, file_ext)


def open_file(f, file_ext):
    if file_ext.lower() == '.json':
        return json.load(f)
    elif file_ext.lower() == '.yml' or file_ext.lower() == '.yaml':
        return yaml.safe_load(f)
    else:
        raise ValueError('This file type is not supported!')
