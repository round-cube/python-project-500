def stylish(d_list, lvl=0):
    res = []
    res.append('{\n')
    ind = ' ' * 2
    ind = ind + ind * 2 * lvl
    d_list.sort(key=lambda x: x['name'])

    for node in d_list:
        op = ' '
        if node['status'] == 'nested':
            data = stylish(node['children'], lvl + 1)
        elif node['status'] == 'changed':
            data = format_data(node['data before'], ind)
            res.append(f"{ind}- {node['name']}: {data}\n")
            data = format_data(node['data after'], ind)
            op = '+'
        else:
            data = format_data(node['data'], ind)
            if node['status'] == 'added':
                op = '+'
            elif node['status'] == 'deleted':
                op = '-'
        if not node['status']:
            raise ValueError('Invalid type!')
        res.append(f"{ind}{op} {node['name']}: {data}\n")
    res.append(ind[:-2] + '}')
    return ''.join(res)


def format_data(data, ind):
    if type(data) is dict:
        ind = ind + '    '
        res = '{\n'
        for key in data.keys():
            value = format_data(data[key], ind)
            res = res + ind + '  ' + key + ': ' + value + '\n'
        res = res + ind[:-2] + '}'
    elif data is False or data is True:
        res = str(data).lower()
    elif data is None:
        res = 'null'
    else:
        res = str(data)
    return res
