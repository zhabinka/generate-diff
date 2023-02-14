import json
import yaml


def parse(data, format_name):
    if format_name == 'json':
        return json.load(data)
    elif format_name in {'yml', 'yaml'}:
        return yaml.safe_load(data)
    else:
        raise ValueError(f'Неверный формат файла: {format_name}')
