def make_request(keys, values):

    dict_out = {}

    if len(keys) != len(values):
        return {}

    for k, v in zip(keys, values):
        dict_out[k] = v
    
    return dict_out


print(make_request([1, 2, 3], ["a", "b", "c"]))
