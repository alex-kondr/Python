from pathlib import Path

path = Path('G:/Мій диск/Мої проекти/Python/txt.txt')

def read_employees_from_file(path):

    fh = open(path, "r")

    employees_list = [line[:-1] if "\n" in line else line for line in fh.readlines()]

    fh.close()

    print(employees_list)

read_employees_from_file(path)