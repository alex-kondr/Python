data = [1, 2, 3]

def all_sub_lists(data):
    sub_lists = [[]]

    l = len(data)

    for j in range(1, l+1):
        for i in range(j):
            sub_lists.append(data[i:j])

    sub_lists.sort()

    return sub_lists


print(all_sub_lists(data))
