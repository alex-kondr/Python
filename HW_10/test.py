from collections import UserDict, UserList


class Field:
    pass


class AddressBook(UserDict, Field):

    ID = 1

    def add_record(self, record):

        self.data.update({record.name.value:record})
        AddressBook.ID += 1

    def get_contact(self, id):
        pass

    def list_contacts(self):
        return self.data


class Name(Field):

    def __init__(self, name):
        self.value = name


class Phone(Field):
    pass


class Record(Field):

    def __init__(self, name):
        self.name = name

    def add_contact(self):
        pass

    def change_contact(self):
        pass

    def remove_contact(self, id):
        pass
