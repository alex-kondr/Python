def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    output_text = ""
    j = 1

    for i in range(len(text)):

        if text[i-j] == start and not text[i] == end:
            output_text += text[i]
            j += 1

    return output_text


print('Example:')
print(between_markers('What is >apple<', '>', '<'))

assert between_markers('What is >apple<', '>', '<') == 'apple'
assert between_markers('What is [apple]', '[', ']') == 'apple'
assert between_markers('What is ><', '>', '<') == ''
assert between_markers('[an apple]', '[', ']') == 'an apple'

print("The mission is done! Click 'Check Solution' to earn rewards!")
