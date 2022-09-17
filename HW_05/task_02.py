articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):

    new_list_of_dict = []

    for item in articles_dict:

        for key_item, val in item.items():

            if (key_item == "title" or key_item == "author"):

                if letter_case and val.find(key) > -1:

                    new_list_of_dict.append(item)
                    break

                elif not letter_case and val.upper().find(key.upper()) > -1:

                    new_list_of_dict.append(item)
                    break

    return new_list_of_dict