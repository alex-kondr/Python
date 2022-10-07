from pathlib import Path
import re

path = Path('G:/Мій диск/Мої проекти/Python/txt.txt')

def get_cats_info(path):

    cats_list = []

    with open(path) as file:
        while True:
            line = file.readline()

            if not line:
                break

            data_list = re.findall("[\w]+", line)
            cats_list.append({"id": data_list[0],
                              "name": data_list[1],
                              "age": data_list[2]
                            })
    print(cats_list)

get_cats_info(path)
