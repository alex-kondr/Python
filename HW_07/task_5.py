s = "    asdf llkt. ouutt ff.   fdsf! klsdsd? jsjdjjjjoo    "


def capital_text(s):

    output = ""
    a = [".", "!", "?"]

    first_char = True

    for char in s:

        if char.isalpha() and first_char:
            char = char.upper()
            first_char = False
            
        if char in a:
            first_char = True
        
        output += char

    return output

capital_text(s)