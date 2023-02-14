from gendiff.format.stylish import format as stylish
from gendiff.format.plain import format as plain
from gendiff.format.json import format as json


FORMATTERS = (JSON, PLAIN, STYLISH) = (
    'json', 'plain', 'stylish'
)

__all__ = ('json', 'plain', 'stylish')
