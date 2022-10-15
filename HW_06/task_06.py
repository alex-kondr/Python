from pathlib import Path

path = Path("G:/Мій диск/Мої проекти/Python/ingredients.csv")


def get_recipe(path, search_id):

    with open(path) as file:

        for line in file.readlines():

            if search_id in line:
                text = line.replace("\n", "")
        
                find_end_id = text.find(",")
                find_end_name = text.find(",", find_end_id+1)

                id = text[:find_end_id]
                name = text[find_end_id+1:find_end_name]
                ingredients = text[find_end_name+1:].split(",")

                return {"id": id,
                        "name": name,
                        "ingredients": ingredients}




print(get_recipe(path, "60b90c3b13067a15887e1ae7"))
