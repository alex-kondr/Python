from pathlib import Path

def get_employees_by_profession(path, profession):

    new_lines = []

    with open(path, "r") as file:
        lines = file.readlines()

        for line in lines:
            if line.find(profession) > -1:
                new_lines.append(line)

    return "".join(new_lines)\
             .replace("\n", "")\
             .replace(profession, "")\
             .strip()

path = Path("1.txt")

a = get_employees_by_profession(path, "courier")

print(a)
print(len(a))
