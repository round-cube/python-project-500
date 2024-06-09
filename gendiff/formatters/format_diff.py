from gendiff.formatters.stylish import create_stylish
from gendiff.formatters.plain import create_plain
from gendiff.formatters.json import create_json


def format_diff(l_diff, f_name):
    if f_name == 'stylish':
        return create_stylish(l_diff)
    elif f_name == 'plain':
        return create_plain(l_diff)
    elif f_name == 'json':
        return create_json(l_diff)
    raise ValueError('Format not found!')
