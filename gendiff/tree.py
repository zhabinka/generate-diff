NESTED, UNCHANGED, CHANGED = 'nested', 'unchanged', 'changed'
REMOVED, ADDED = 'removed', 'added'


def build_diff(data1, data2):
    result = {}

    for key in data1.keys() & data2.keys():
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = (NESTED, build_diff(data1[key], data2[key]))
        elif data1[key] == data2[key]:
            result[key] = (UNCHANGED, data2[key])
        else:
            result[key] = (CHANGED, (data1[key], data2[key]))

    def update_result_with(status, dict1, dict2):
        result.update(
            {key: (status, dict1[key]) for key in dict1.keys() - dict2.keys()}
        )

    update_result_with(REMOVED, data1, data2)
    update_result_with(ADDED, data2, data1)
    return result
