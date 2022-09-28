def correct_sentence(text: str) -> str:
    """
    returns a corrected sentence which starts with a capital letter
    and ends with a dot.
    """
    # your code here
    first_char = text[0].upper()

    if text[len(text) - 1] == ".":
        return first_char + text[slice(1, len(text))]
    
    else:
        return first_char + text[slice(1, len(text))] + "."
    



print("Example:")
print(correct_sentence("greetings, friends"))

assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends") == "Greetings, friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."

print("The mission is done! Click 'Check Solution' to earn rewards!")
