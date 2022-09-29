def backward_string_by_word(text: str) -> str:
    # your code here
    word_temp1 = ""
    text_reverse_by_word = ""

    for char in text:

        if char.isalpha():
            word_temp1 = char + word_temp1
            
        else:
            text_reverse_by_word += word_temp1 + char
            word_temp1 = ""

    if word_temp1:
        text_reverse_by_word += word_temp1

    return text_reverse_by_word


print("Example:")
print(backward_string_by_word("hello world"))

assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")
