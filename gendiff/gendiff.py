#!/usr/bin/env python3

# from gendiff.generate_diff import generate_diff
from gendiff.tools.argparse import parser_arg

from gendiff.tools.parse_file import get_dict_from_file
from gendiff.tools.diff import diff
from gendiff.formatters.format_diff import format_diff


def main():
    path_file1, path_file2, format_name = parser_arg()
    diff = generate_diff(path_file1, path_file2, format_name)
    print(diff)


def generate_diff(path_file1, path_file2, format_name='stylish'):
    d1 = get_dict_from_file(path_file1)
    d2 = get_dict_from_file(path_file2)
    l_diff = diff(d1, d2)
    return format_diff(l_diff, format_name)


if __name__ == '__main__':
    main()