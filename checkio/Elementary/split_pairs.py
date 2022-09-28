from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    # your code here
    list = []
    i = 0
    if len(text) > 1:
        while i <= len(text) // 2:
            list.append(text[slice(i, i+2)])
            i += 2

    if len(text) % 2:
        list.append(text[len(text) - 1] + "_")

    return list


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
