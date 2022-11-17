from collections import UserDict
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
            return "Birthday not specified"

        now_date = datetime.now()
        birthday = self.birthday.value.replace(year=now_date.year)

        return  (birthday - now_date).days

    def list_phones(self) -> str:
        phones = ""

        for i, phone in enumerate(self.phones):
            if i > 0:
                phones += "|{:^3}|{:^10}|".format(" ", " ")
            
            phones += "{:^3}|{:^13}|\n".format(i, phone.value)         

        return phones

    def remove_phone(self, number_in_list: int):
        return self.phones.pop(number_in_list)


class AddressBook(UserDict):

    def __str__(self):
        message = "\n|{:^3}|{:^10}|{:^3}|{:^13}|\n".format(
            "№", "User", "№", "Phone")
        message += "-" * 35 + "\n"

        for i, (name, record) in enumerate(self.data.items()):
            message += "|{:^3}|{:^10}|{:^13}".format(
                i, name, record.list_phones())
        
        return message

    def add_record(self, data: str):

        name, phone = data.split()
        new_phone = Phone()
        new_phone.value = phone
        record = self.data.get(name, Record(Name(name)))
        record.add_phone(new_phone)
        self.data.update({record.name.value: record})        

        return f"The mobile phone {phone} is added to "\
            f"the user '{name}' in the phone book."

    def change_phone_in_record(self, name: str):
        record = self.data.get(name)

        if not record:
            return f"User '{name}' not found on phone book."

        print("\nWhat number do you want change")
        print(self.get_contact(name))
        number = int(
            input("Select the number in the order you want to change: "))
        mobile_phone = input("\nEnter new mobile number: ")
        record.change_phone(number, mobile_phone)

        return f"User '{name}' changed mobile phone on address book."
        

    def iterator(self, N: int):
        i = 0
        data = AddressBook()
        
        for n, (name, record) in enumerate(self.data.items()):
            data.update({name: record})
            i += 1

            if i == N or n == len(self.data) - 1:
                yield data
                data.clear()
                i = 0

    def get_contact(self, name: str):
        data = AddressBook()
        data.update({name: self.data.get(name)})

        return data

    def list_contacts(self):
        
        n = int(input("How many records to show at once. 0 - show all: "))        
        generator = self.iterator(n)

        while True:
            try:
                data1 = None
                data = data1 if data1 else next(generator)
                print(data)             
                data1 = next(generator)
                input("Press enter to download the next part ")               

            except StopIteration:
                return ""
