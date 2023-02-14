import argparse
from gendiff import format


def get_formatter(arg):
    if arg == format.JSON:
        return format.json
    elif arg == format.PLAIN:
        return format.plain
    elif arg == format.STYLISH:
        return format.stylish
    else:
        msg = f'Incorrect format, must be {", ".join(format.FORMATTERS)}'
        raise argparse.ArgumentTypeError(msg)


def parse_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default=format.STYLISH,
                        help='set format of output: json, plain, stylish',
                        type=get_formatter)
    return parser.parse_args()
