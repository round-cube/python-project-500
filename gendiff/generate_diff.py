from gendiff.tools.parse_file import get_dict_from_file
from gendiff.tools.diff import diff
from gendiff.formatters.stylish import stylish


def generate_diff(path_file1, path_file2, format_name='stylish'):
    d1 = get_dict_from_file(path_file1)
    d2 = get_dict_from_file(path_file2)
    l_diff = diff(d1, d2)
    return stylish(l_diff)
