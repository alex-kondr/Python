def first_word(text: str) -> str:
    """
    function returns the first word in a given text.
    """
    # your code here
    replace_char = [",", ".", "!", "?"]
    new_text = text

    for char in replace_char:
        new_text = new_text.replace(char, " ").strip()
    
    list_words = new_text.split(" ")

    return list_words[0]


print("Example:")
print(first_word("Hello world"))

assert first_word("Hello world") == "Hello"
assert first_word(" a word ") == "a"
assert first_word("don't touch it") == "don't"
assert first_word("greetings, friends") == "greetings"
assert first_word("... and so on ...") == "and"
assert first_word("hi") == "hi"

print("The mission is done! Click 'Check Solution' to earn rewards!")
