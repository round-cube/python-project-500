import pytest
from gendiff.generate_diff import generate_diff
from pathlib import Path


@pytest.mark.parametrize(
    "file1, file2, file_answer, form_name",
    [
        ('file1.json', 'file2.json', 'corr_answer_stylish.txt', 'stylish'),
        ('file1.yml', 'file2.yml', 'corr_answer_stylish.txt', 'stylish'),
        ('file1.json', 'file2.json', 'corr_answer_plain.txt', 'plain'),
        ('file1.yml', 'file2.yml', 'corr_answer_plain.txt', 'plain'),
    ]
)


def test_generate_diff(file1, file2, file_answer, form_name):
    p = Path(Path() / 'tests' / 'fixtures' / file_answer)
    with open(p) as f:
        corr_answer = f.read()
    assert generate_diff(file1, file2, form_name) == corr_answer
