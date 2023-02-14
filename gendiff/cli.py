import argparse
from gendiff import format


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default=format.STYLISH,
                        help='set format of output: json, plain, stylish',
                        )
    return parser.parse_args()
