from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import f_json


def format_diff(l_diff, f_name):
    if f_name == 'stylish':
        return stylish(l_diff)
    elif f_name == 'plain':
        return plain(l_diff)
    elif f_name == 'json':
        return f_json(l_diff)
    else:
        return 'Format not found!'
