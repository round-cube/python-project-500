def plain(d_list):
    d_list.sort(key=lambda x: x['name'])
    res = get_diff_plain(d_list)
    return '\n'.join(res)


def get_diff_plain(d_list, path=''):
    res = []
    for node in d_list:
        path_to_ch = path + node['name']
        if node['status'] == 'nested':
            path_to_ch = path_to_ch + '.'
            diff = get_diff_plain(node['children'], path_to_ch)
            res.extend(diff)
        elif node['status'] == 'added':
            ch = create_change(node['data'])
            diff = (
                f"Property '{path_to_ch}' was added "
                f"with value: {ch}"
            )
            res.append(diff)
        elif node['status'] == 'deleted':
            ch = create_change(node['data'])
            diff = "Property '{}' was removed".format(path_to_ch)
            res.append(diff)
        elif node['status'] == 'changed':
            ch_bef = create_change(node['data before'])
            ch_aft = create_change(node['data after'])
            diff = (
                f"Property '{path_to_ch}' was updated. "
                f"From {ch_bef} to {ch_aft}"
            )
            res.append(diff)
        if not node['status']:
            raise ValueError('Invalid type!')
    return res


def create_change(data):
    """Анализирует данные узла. Возвращает его в правильном формате \
в виде строки."""
    if type(data) is dict or type(data) is list:
        res = '[complex value]'
    elif data is False or data is True:
        res = str(data).lower()
    elif data is None:
        res = 'null'
    elif type(data) is str:
        res = "'{}'".format(data)
    else:
        res = '{}'.format(data)
    return res
