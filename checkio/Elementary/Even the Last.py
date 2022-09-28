def checkio(array: list[int]) -> int:
    # your code here
    sum = 0

    for i in range(0, len(array), 2):
        sum += array[i]
        
    return None


print("Example:")
print(checkio([0, 1, 2, 3, 4, 5]))

assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
