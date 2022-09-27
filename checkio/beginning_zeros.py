def beginning_zeros(a: str) -> int:
    # your code here
    count_zeros = 0
    for ch in a:

        if ch == "0":
            count_zeros += 1

        else:
            break

    return count_zeros


print('Example:')
print(beginning_zeros('10'))

assert beginning_zeros('100') == 0
assert beginning_zeros('001') == 2
assert beginning_zeros('100100') == 0
assert beginning_zeros('001001') == 2
assert beginning_zeros('012345679') == 1
assert beginning_zeros('0000') == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
