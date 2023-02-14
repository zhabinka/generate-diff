import argparse
from gendiff import format
from gendiff.formatter import get_formatter


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default=format.STYLISH,
                        help='set format of output: json, plain, stylish',
                        type=get_formatter)
    return parser.parse_args()
