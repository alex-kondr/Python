def nearest_value(values: set, one: int) -> int:
    # your code here
    distance = 100

    for num in values:

        if abs(num - one) < distance:

            nearest_num = num
            distance = abs(num - one)

        elif abs(num - one) == distance and num < nearest_num:
            nearest_num = num

    return nearest_num


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({0, -2}, -1))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({-6, -2, 4, 7, 12, 17}, -4) == -6
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({5}, 5) == 5
    assert nearest_value({5}, 7) == 5
    print("Coding complete? Click 'Check' to earn cool rewards!")
