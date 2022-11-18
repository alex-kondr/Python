from datetime import datetime
import re


class Field:

    def __init__(self, value):
        self._value = None
        self.value = value

    def __str__(self):
        return f"{type(self)}: {self.value}"

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Birthday(Field):

    @Field.value.setter
    def value(self, data: str):

        birthday = re.search(r"\d{2}\.\d{2}", data)

        if not birthday:
            raise ValueError("Birthday not valid.\n"\
                "The Birthday should look like '01.01'")
        
        self._value = datetime.strptime(birthday.group(), "%d.%m")


class Name(Field):

    @Field.value.setter
    def value(self, value: str):
        if type(value) == str:
            self._value = value


class Phone(Field):

    @Field.value.setter
    def value(self, phone: str):
        new_phone = re.search(r"\+380\d{9}", phone)

        if not new_phone:
            raise ValueError("Phone number not valid.\n"\
                "The phone number should look like +380123456789")
        
        self._value = new_phone.group()


class Record():

    def __init__(self, name: Name):
        self.birthday = None
        self.name = name
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, number_in_list: int, new_phone: str):        
        self.phones[number_in_list].value = new_phone

    def days_to_birthday(self):

        if not self.birthday:
            raise ValueError("Birthday not specified")

        now_date = datetime.now()
        birthday = self.birthday.value.replace(year=now_date.year)

        return  (birthday - now_date).days + 1

    def list_phones(self) -> str:
        phones = ""

        for i, phone in enumerate(self.phones):
            if i > 0:
                phones += "|{:^3}|{:^10}|".format(" ", " ")
            
            phones += "{:^3}|{:^13}|\n".format(i, phone.value)         

        return phones

    def remove_phone(self, number_in_list: int):
        return self.phones.pop(number_in_list)
