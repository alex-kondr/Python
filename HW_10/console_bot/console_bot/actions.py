from collections import UserDict 
from input_error import input_error
import re


USERS = {}


class AddressBook(UserDict):
    pass


class Field:
    pass


class Name:

    def __init__(self, name):
        self.name = name
        

class Record:

    def __init__(self, name):
        self.name = name

    def add(self):
        pass

    def change(self):
        pass

    def del_record(self):
        pass


@input_error
def add(data: str) -> str:

    name, phone = data.split()
    phone = re.search(r"\+380\d{9}", phone)

    if name not in USERS and phone:
        USERS.update({name: phone.group()})
        return f"User '{name}' added to phone book"

    return f"User '{name}' already exist or phone number not valid.\n"\
        "The phone number should look like +380123456789"

@input_error
def change(data: str) -> str:

    name, phone = data.split()
    phone = re.search(r"\+380\d{9}", phone)

    if name in USERS and phone:
        USERS.update({name: phone.group()})
        return f"User '{name}' changed on phone book"

    return f"User '{name}' not found on phone book or phone number not valid.\n"\
        "The phone number should look like +380123456789"

@input_error
def phone(data: str) -> str:

    name = data
    message = "|{:^10}|{:^13}|\n".format("User", "Phone")
    message += "-" * 26 + "\n"
    message += "|{:^10}|{:<13}|".format(name, USERS[name])

    return message

@input_error
def show_all() -> str:

    message = "|{:^10}|{:^13}|\n".format("User", "Phone")
    message += "-" * 26 + "\n"

    for name, phone in USERS.items():
        message += "|{:^10}|{:<13}|\n".format(name, phone)

    return message
