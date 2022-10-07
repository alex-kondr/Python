from pathlib import Path

path = Path('G:/Мій диск/Мої проекти/Python/txt.txt')

def add_employee_to_file(record, path):

    file = open(path, "a")
    file.write(record + "\n")
    file.close()

add_employee_to_file("Mikle,36", path)
