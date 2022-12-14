from collections import UserDict


class Field:
    pass


class Name(Field):

    def __init__(self, name: str):
        self.value = name


class Phone(Field):

    def __init__(self):    
        self.mobile_phone = ""
        self.home_phone = ""
        self.email = ""


class Record():

    def __init__(self, name: Name):
        self.name = name
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, number_in_list: int, new_phone: str):        
        self.phones[number_in_list].mobile_phone = new_phone

    def remove_phone(self, number_in_list: int):
        return self.phones.pop(number_in_list)


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    def get_contact(self, name: str):
        return self.data.get(name)

    def list_contacts(self) -> dict:
        return self.data
