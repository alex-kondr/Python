def sequence_buttons(string):

    numb_leter = {(".", ",", "?", "!", ":"): "1",
                  ("A", "B", "C"): "2",
                  ("D", "E", "F"): "3",
                  ("G", "H", "I"): "4",
                  ("J", "K", "L"): "5",
                  ("M", "N", "O"): "6",
                  ("P", "Q", "R", "S"): "7",
                  ("T", "U", "V"): "8",
                  ("W", "X", "Y", "Z"): "9",
                  (" "): "0"}

    comb = ""
    
    for char in string:
        for k, v in numb_leter.items():
            if char in k:
                comb += v * (k.index(char) + 1)
                continue
            elif char.upper() in k:
                comb += v.lower() * (k.index(char.upper()) + 1)

    return comb


print(sequence_buttons("Hello word!"))


