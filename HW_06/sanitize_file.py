from pathlib import Path


source = Path("C:/Users/TrueConf/Documents/Python/HW_06/source.txt")

output = Path("C:/Users/TrueConf/Documents/Python/HW_06/output.txt")

def sanitize_file(source, output):
    output_text = ""

    with open(source, "r") as file:
        temp_text = ""

        for line in file.readlines():
            temp_text += line

    for char in temp_text:
        if not char.isdigit():
            output_text += char       

    with open(output, "w") as file:
        file.write(output_text)

sanitize_file(source, output)
