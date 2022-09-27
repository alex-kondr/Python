def sum_numbers(text: str) -> int:
    # your code here
    words_list = text.split(" ")
    sum = 0

    for num_in_text in words_list:

        if num_in_text.isnumeric():
            sum += int(num_in_text)

    return sum


print("Example:")
print(sum_numbers("hi"))

assert sum_numbers("hi") == 0
assert sum_numbers("who is 1st here") == 0
assert sum_numbers("my numbers is 2") == 2
assert (
    sum_numbers(
        "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
    )
    == 3755
)
assert sum_numbers("5 plus 6 is") == 11
assert sum_numbers("") == 0

print("The mission is done! Click 'Check Solution' to earn rewards!")
