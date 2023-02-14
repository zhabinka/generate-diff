from gendiff import tree


def indent(depth):
    return '  ' * depth


def to_str(value, depth):
    if isinstance(value, bool):
        return 'true' if value else 'false'

    if value is None:
        return 'null'

    if not isinstance(value, dict):
        return value
    result = f'\n{indent(depth + 3)}'.join([f'{k}: {to_str(v, depth + 2)}' for k, v in value.items()])
    return f'{{\n{indent(depth + 3)}{result}\n{indent(depth + 1)}}}'


def render(diff_data, depth=1):
    lines = []
    for key, (status, value) in sorted(diff_data.items()):
        def store(symbol, value):
            lines.append(
                f'{indent(depth)}{symbol} {key}: {to_str(value, depth)}'
            )

        if status == tree.NESTED:
            lines.append(
                f'{indent(depth)}  {key}: '
                f'{{\n{render(value, depth + 2)}\n{indent(depth + 1)}}}'
            )
        elif status == tree.UNCHANGED:
            store(' ', value)
        elif status == tree.CHANGED:
            old, new = value
            store('-', old)
            store('+', new)
        elif status == tree.REMOVED:
            store('-', value)
        elif status == tree.ADDED:
            store('+', value)

    return '\n'.join(lines)


def format(diff):
    return f'{{\n{render(diff)}\n}}'
