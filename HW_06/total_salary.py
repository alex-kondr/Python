from pathlib import Path
import re

path = Path('G:/Мій диск/Мої проекти/Python/txt.txt')



def total_salary(path):
    fh = open(path, "r")

    sum = 0

    while True:
        line = fh.readline()
        if not line:
            break

        salary = re.findall(r"[\d]+", line)[0]
        sum += float(salary)

    fh.close()

    return sum

total_salary(path)