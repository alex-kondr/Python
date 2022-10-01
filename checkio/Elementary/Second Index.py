def second_index(text: str, symbol: str) -> int:
    """
    returns the second index of a symbol in a given text
    """
    # your code here
    first_index = text.find(symbol)
    second_index = text.find(symbol, first_index+1)

    return second_index if second_index > -1 else None


print("Example:")
print(second_index("sims", "s"))

assert second_index("sims", "s") == 3
assert second_index("find the river", "e") == 12
assert second_index("hi", " ") == None
assert second_index("hi mayor", " ") == None
assert second_index("hi mr Mayor", " ") == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")
