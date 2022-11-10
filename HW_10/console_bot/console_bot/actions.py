from address_book import AddressBook, Name, Phone, Record
from input_error import input_error
import re

address_book = AddressBook()


@input_error
def add(data: str) -> str:

    name, phone = data.split()
    phone = re.search(r"\+380\d{9}", phone)
    

    if name and phone:
        new_phone = Phone()
        new_phone.mobile_phone = phone.group()

        # if address_book.get_contact(name):
        #     record = address_book.get_contact(name)

        name = Name(name)
        record = Record(name)
        record.add_phone(new_phone)
        address_book.add_record(record)

        print(address_book.list_contacts, address_book.count)
        return f"User '{name.value}' added to phone book"
    
        # {record.name.value: record}
    # if name not in USERS and phone:
    #     USERS.update({name: phone.group()})
    #     return f"User '{name}' added to phone book"

    return f"User '{name}' already exist or phone number not valid.\n"\
        "The phone number should look like +380123456789"


@input_error
def change(data: str) -> str:

    name, phone = data.split()
    phone = re.search(r"\+380\d{9}", phone)

    # if name in USERS and phone:
    #     USERS.update({name: phone.group()})
    #     return f"User '{name}' changed on phone book"

    return f"User '{name}' not found on phone book or phone number not valid.\n"\
        "The phone number should look like +380123456789"


@input_error
def phone(data: str) -> str:

    name = data
    message = "|{:^10}|{:^13}|\n".format("User", "Phone")
    message += "-" * 26 + "\n"
    # message += "|{:^10}|{:<13}|".format(name, USERS[name])

    return message


@input_error
def show_all() -> str:

    message = "|{:^10}|{:^13}|\n".format("User", "Phone")
    message += "-" * 26 + "\n"

    # for name, phone in USERS.items():
    #     message += "|{:^10}|{:<13}|\n".format(name, phone)

    return message

