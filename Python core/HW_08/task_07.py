import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

cats = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]

cats1 = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]


def convert_list(cats):

    list_cats = []

    if isinstance(cats[0], tuple):

        for cat in cats:
            list_cats.append(cat._asdict())

    elif isinstance(cats[0], dict):

        for cat in cats:
            list_cats.append(Cat(**cat))

    return list_cats


print(convert_list(cats1))
