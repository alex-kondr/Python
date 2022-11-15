from collections import UserDict
from datetime import datetime
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

        birthday = re.search("\d{2}\.\d{2}", birthday)  #type: ignore

        if not birthday:
            raise ValueError("Birthday not valid.\n"\
                "The Birthday should look like '01.01'")
        
        self._value = datetime.strptime(birthday.group(), "%d.%m")  #type: ignore


class Name(Field):

    def __init__(self, name: str):
        super().__init__()
        self.value = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, name: str):
        if type(name) == str:
            self._value = name


class Phone(Field):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, phone: str):
        phone = re.search(r"\+380\d{9}", phone)  # type: ignore

        if not phone:
            raise ValueError("Phone number not valid.\n"\
                "The phone number should look like +380123456789")
        
        self._value = phone.group()  # type: ignore


class Record():

    def __init__(self, name: Name):
        self.birthday = Birthday()
        self.name = name
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, number_in_list: int, new_phone: str):        
        self.phones[number_in_list].mobile_phone = new_phone

    def days_to_birthday(self):

        if not self.birthday.value:
            return "Birthday not specified"

        now_date = datetime.now()
        birthday = self.birthday.value.replace(year=now_date.year)

        return  (birthday - now_date).days        

    def remove_phone(self, number_in_list: int):
        return self.phones.pop(number_in_list)


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})

    def iterator(self, N: int):
        i = 0
        data = {}
        
        for n, (name, record) in enumerate(self.data.items()):
            data.update({name: record})
            i += 1

            if i == N or n == len(self.data) - 1:
                yield data
                data.clear()
                i = 0

    def get_contact(self, name: str):
        return self.data.get(name)

    def list_contacts(self) -> dict:
        return self.data

