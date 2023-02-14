import os
import json
import pytest
from gendiff import format
from gendiff.diff import generate_diff


def get_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def get_file_data(file_name):
    return read(get_path(file_name))


FILE1 = get_path('file1.json')
FILE2 = get_path('file2.json')
FILE3 = get_path('file1.yml')
FILE4 = get_path('file2.yml')

test_cases_diff = [
    (
        generate_diff(FILE1, FILE2, format.STYLISH),
        get_file_data('result_stylish')
    ),
    (
        generate_diff(FILE1, FILE2, format.PLAIN),
        get_file_data('result_plain')
    ),
    (
        json.loads(generate_diff(FILE1, FILE2, format.JSON)),
        json.loads(get_file_data('result.json'))
    ),
    (
        generate_diff(FILE3, FILE4, format.STYLISH),
        get_file_data('result_stylish')
    ),
    (
        generate_diff(FILE3, FILE4, format.PLAIN),
        get_file_data('result_plain')
    ),
    (
        json.loads(generate_diff(FILE3, FILE4, format.JSON)),
        json.loads(get_file_data('result.json'))
    )
]


@pytest.mark.parametrize('test_input, expected_result', test_cases_diff)
def test_generate_diff(test_input, expected_result):
    assert test_input == expected_result
