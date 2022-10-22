data = [1, 2, 3]

def all_sub_lists(data):
    sub_lists = [[]]

    l = len(data)

    for j in range(1, l+1):
        for i in range(j):
            sub_lists.append(data[i:j])

    sub_lists.sort(key=func)

    return sub_lists

def func(el):
    return len(el)


print(all_sub_lists(data))
