#1

class SerializationInterface(type):
    pass

#2


class Meta(type):
    children_number = 0
    class_number = 0

    def __new__(*args):
        args[0].children_number += 1       

        return type.__new__(*args)

    def __init__(self, *args):
        self.class_number = Meta.class_number
        Meta.class_number += 1


Meta.children_number = 0

class Cls1(metaclass=Meta):

    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):

    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(""), Cls2("")
assert (a.class_number, b.class_number) == (0, 1)
