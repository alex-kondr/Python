from collections import UserDict
from datetime import datetime, timedelta
import re


class Field:
    def __init__(self):
        self._value = None


class Birthday(Field):
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, birthday: str):
        value = datetime.strptime(birthday, "%d.%m")


class Name(Field):

    def __init__(self, name: str):
        super().__init__()
        self.value = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, name):
        if type(name) == str:
            self._value = name


class Phone(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, phone):
        phone = re.search(r"\+380\d{9}", phone)

        if not phone:
            raise ValueError("Phone number not valid.\n"\
                "The phone number should look like + 380123456789")
        
        self._value = phone.group()


class Record():

    def __init__(self, name: Name):
        self.name = name
        self.phones = []

    def __next__(self):
        pass

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, number_in_list: int, new_phone: str):        
        self.phones[number_in_list].mobile_phone = new_phone

    def days_to_birthday(self):
        pass

    def remove_phone(self, number_in_list: int):
        return self.phones.pop(number_in_list)


class AddressBook(UserDict):

    def __iter__(self):
        pass

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    def get_contact(self, name: str):
        return self.data.get(name)

    def list_contacts(self) -> dict:
        return self.data
