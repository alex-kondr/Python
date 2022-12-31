#1
from abc import ABCMeta, abstractmethod
import json
import pickle

class SerializationInterface(metaclass=ABCMeta):
    
    @abstractmethod
    def serialize(self, filename):
        pass


class SerializeJSON(SerializationInterface):

    def serialize(self, filename, data):

        with open(filename, "w", newline="") as fh:
            json.dump(data, fh)


class SerializeBin(SerializationInterface):

    def serialize(self, filename):

        with open(filename, "wb") as fh:
            pickle.dump(self, fh)


#2
class Meta(type):
    children_number = 0
    class_number = 0

    def __new__(*args):
        Meta.children_number += 1
        print("new")

        return type.__new__(*args)

    def __init__(self, *args):
        self.class_number = Meta.class_number
        Meta.class_number += 1


# Meta.children_number = 0


class Cls1(metaclass=Meta):

    def __init__(self, data):
        self.data = data

# print(Meta.children_number)

class Cls2(metaclass=Meta):

    def __init__(self, data):
        self.data = data

# print(Meta.children_number)


# assert (Cls1.class_number, Cls2.class_number) == (0, 1)
# a, b = Cls1(""), Cls2("")
# assert (a.class_number, b.class_number) == (0, 1)

