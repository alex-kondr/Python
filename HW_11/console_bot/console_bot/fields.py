from datetime import datetime
import re


class Field:

    def __init__(self):
        self._value = None

    def __str__(self):
        return f"{type(self)}: {self.value}"

    @property
    def value(self):
        return self._value


class Birthday(Field):

    @Field.value.setter
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

    @Field.value.setter
    def value(self, name: str):
        if type(name) == str:
            self._value = name


class Phone(Field):

    @Field.value.setter
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
        self.phones[number_in_list].value = new_phone

    def days_to_birthday(self):

        if not self.birthday.value:
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
