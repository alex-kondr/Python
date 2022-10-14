from pathlib import Path


path = Path("HW_06/output.txt")

def get_credentials_users(path):
    lines = []

    with open(path, "rb") as file:

        for line in file.readlines():
            lines.append(line.decode().replace("\n", ""))

    return lines

print(get_credentials_users(path))
