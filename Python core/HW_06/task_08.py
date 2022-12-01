from pathlib import Path


output = Path("HW_06/output.txt")


source = [
            {
                "name": "Kovalchuk Oleksiy",
                "specialty": 301,
                "math": 175,
                "lang": 180,
                "eng": 155,
            },
            {
                "name": "Ivanchuk Boryslav",
                "specialty": 101,
                "math": 135,
                "lang": 150,
                "eng": 165,
            },
            {
                "name": "Karpenko Dmitro",
                "specialty": 201,
                "math": 155,
                "lang": 175,
                "eng": 185,
            },
        ]


def save_applicant_data(source, output):

    text_to_file = ""

    for dict in source:        

        for value in dict.values():
            text_to_file += str(value) + ","
        
        text_to_file = text_to_file[:-1] + "\n"

    with open(output, "w") as file:
        file.write(text_to_file)

save_applicant_data(source, output)
