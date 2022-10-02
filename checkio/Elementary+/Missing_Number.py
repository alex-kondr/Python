def missing_number(items: list[int]) -> int:
    # your code here
    items.sort()
    difference = [items[i] - items[i-1] for i in range(len(items))]
    difference.pop(0)
    difference.sort()
    difference = difference[0]

    for i in range(len(items)):
        if i > 0 and items[i] - items[i-1] != difference:
            lost_number = items[i-1] + difference
            break  

    return lost_number


print("Example:")
print(missing_number([1, 4, 2, 5]))

assert missing_number([1, 4, 2, 5]) == 3
assert missing_number([2, 6, 8]) == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
