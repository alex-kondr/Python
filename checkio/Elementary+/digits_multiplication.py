def checkio(number: int) -> int:

    result = 1

    for num in str(number):
        if int(num) > 0:
            result *= int(num)
    
    return result


print("Example:")
print(checkio(123405))

assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
