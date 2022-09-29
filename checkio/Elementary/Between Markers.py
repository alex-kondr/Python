def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    # your code here
    # output_text = ""
    # j = 1

    # for i in range(len(text)):

    #     if text[i-j] == begin and not text[i] == end:
    #         output_text += text[i]
    #         j += 1

    begin_index = None
    end_index = None

    if begin and text.find(begin) > -1:
        begin_index = text.find(begin) + len(begin)

    if end and text.find(end) > -1:
        end_index = text.find(end)

    text_out = text[begin_index:end_index]

    return text_out


print("Example:")
print(between_markers("Never send a human to do a machine's job.", 'Never', 'do'))

assert between_markers("What is >apple<", ">", "<") == "apple"
assert (
    between_markers("<head><title>My new site</title></head>",
                    "<title>", "</title>")
    == "My new site"
)
assert between_markers("No[/b] hi", "[b]", "[/b]") == "No"
assert between_markers("No [b]hi", "[b]", "[/b]") == "hi"
assert between_markers("No hi", "[b]", "[/b]") == "No hi"
assert between_markers("No <hi>", ">", "<") == ""

print("The mission is done! Click 'Check Solution' to earn rewards!")
