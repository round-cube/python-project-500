from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def format_diff(l_diff, f_name):
    if f_name == 'stylish':
        return stylish(l_diff)
    elif f_name == 'plain':
        return plain(l_diff)
    else:
        return 'Format not found!'
