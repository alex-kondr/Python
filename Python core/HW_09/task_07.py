def normal_name(list_name):

    new_list = []

    for item in map(lambda x: x.title(), list_name):
        new_list.append(item)

    return new_list
