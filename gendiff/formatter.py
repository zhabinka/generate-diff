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
        raise ValueError(msg)
