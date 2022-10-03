from typing import Any, Iterable


def split_list(items: list[Any]) -> Iterable[list[Any]]:
    # your code here
    list_split = [[], []]

    slice_size = len(items) // 2

    if items and len(items) % 2:        
        list_split[0] = items[:slice_size + 1]
        list_split[1] = items[slice_size + 1:]

    elif items and not len(items) % 2:
        list_split[0] = items[:slice_size]
        list_split[1] = items[slice_size:]

    return list_split


print("Example:")
print(list(split_list([1, 2, 3, 4, 5, 6])))

assert list(split_list([1, 2, 3, 4, 5, 6])) == [[1, 2, 3], [4, 5, 6]]
assert list(split_list([1, 2, 3])) == [[1, 2], [3]]
assert list(split_list(["banana", "apple", "orange", "cherry", "watermelon"])) == [
    ["banana", "apple", "orange"],
    ["cherry", "watermelon"],
]
assert list(split_list([1])) == [[1], []]
assert list(split_list([])) == [[], []]

print("The mission is done! Click 'Check Solution' to earn rewards!")
