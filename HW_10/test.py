from collections import UserDict, UserList


class Field:
    pass


class AddressBook(UserDict, Field):

    phone = None
    email = None

    def add_record(self):
        pass


class Name(Field):

    def __init__(self, name):
        self.name = name


class Phone(UserList, Field):

    pass


class Record(Field):

    def __init__(self, name):
        self.name = name

    def add(self):
        pass

    def change(self):
        pass

    def del_record(self):
        pass
