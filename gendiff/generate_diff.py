import json
from pathlib import Path


def get_fixture_path(file_name):
    return Path(Path() / 'tests' / 'fixtures' / file_name)
    # return Path(Path(__file__).parent.absolute() / 'fixtures' / file_name)


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
