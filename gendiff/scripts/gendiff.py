#!/usr/bin/env python3

import argparse
import json
from pathlib import Path


def parser_arg():
    parser = argparse.ArgumentParser(description='Compares two \
    configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def get_fixture_path(file_name):
    return Path(Path.home() / 'python-project-50/gendiff/fixtures' / file_name)


def generate_diff(path_file1, path_file2):
    p1 = get_fixture_path(path_file1)
    p2 = get_fixture_path(path_file2)

    d1 = json.load(open(p1))
    d2 = json.load(open(p2))
    res = {}
    keys = sorted(d1.keys() | d2.keys())
    for key in keys:
        if key in d1 and key not in d2:
            res[f'  - {key}'] = d1[key]
        elif key in d1 and key in d2 and d1[key] != d2[key]:
            res[f'  - {key}'] = d1[key]
            res[f'  + {key}'] = d2[key]
        elif key in d2 and key not in d1:
            res[f'  + {key}'] = d2[key]
        else:
            res[f'    {key}'] = d1[key]

    l = []
    for k, v in res.items():
        l.append(k + ': ' + str(v))
    r = '\n'.join(l)
    return f"{{\n{r}\n}}"


def main():
    path_file1, path_file2, format_name = parser_arg()
    diff = generate_diff(path_file1, path_file2)
    print(diff)


if __name__ == '__main__':
    main()
