from typing import Iterable


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    new_list = []
    try:
        index_border = items.index(border)
        for i in range(index_border, len(items)):
            new_list.append(items[i])
    except ValueError:
        pass
    return new_list


print('Example:')
print(remove_all_before([1, 2, 3, 4, 5], 3))
