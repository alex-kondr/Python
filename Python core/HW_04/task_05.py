def lookup_key(data, value):

    key_list = []

    for key, val in data.items():

        if val == value:
            key_list.append(key)

    return key_list
