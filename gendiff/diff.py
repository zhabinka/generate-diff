import os

from gendiff.tree import build_diff
from gendiff.parsers import parse
from gendiff import format


def get_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension.lower()[1:]


def get_data(file_path):
    return parse(open(file_path), get_format(file_path))


def generate_diff(file_path1, file_path2, formatter=format.STYLISH):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    diff = build_diff(data1, data2)

    return formatter(diff)
