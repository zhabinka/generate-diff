from gendiff import tree


def to_str(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'

    if value is None:
        return 'null'

    if isinstance(value, dict) or isinstance(value, list):
        return "[complex value]"

    elif isinstance(value, str):
        return f"'{value}'"

    return value


def get_full_path(acc, key):
    return '.'.join([*acc, key])


def render(diff_data, acc):
    lines = []
    for key, (status, value) in sorted(diff_data.items()):
        if status == tree.NESTED:
            lines.append(render(value, [*acc, key]))
        elif status == tree.CHANGED:
            old, new = value
            lines.append(
                f"Property '{get_full_path(acc, key)}' was updated. "
                f"From {to_str(old)} to {to_str(new)}"
            )
        elif status == tree.REMOVED:
            lines.append(
                f"Property '{get_full_path(acc, key)}' was removed"
            )
        elif status == tree.ADDED:
            lines.append(
                f"Property '{get_full_path(acc, key)}' "
                f"was added with value: {to_str(value)}"
            )

    return '\n'.join(lines)


def format(diff):
    return render(diff, [])
