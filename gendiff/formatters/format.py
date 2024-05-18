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
