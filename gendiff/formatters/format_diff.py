from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import jjson


def format_diff(l_diff, f_name):
    if f_name == 'stylish':
        return stylish(l_diff)
    elif f_name == 'plain':
        return plain(l_diff)
    elif f_name == 'json':
        return jjson(l_diff)
    raise ValueError('Format not found!')
