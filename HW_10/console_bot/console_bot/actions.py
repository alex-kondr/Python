from address_book import AddressBook, Name, Phone, Record
from input_error import input_error
import re


ADDRESS_BOOK = AddressBook()


@input_error
def add(data: str) -> str:

    name, phone = data.split()
    phone = re.search(r"\+380\d{9}", phone)

    if not ADDRESS_BOOK.get_contact(name) and phone:
        new_phone = Phone()
        new_phone.mobile_phone = phone.group()
        name = Name(name)
        record = Record(name)
        record.add_phone(new_phone)
        ADDRESS_BOOK.add_record(record)
        
        return f"User '{name.value}' added to phone book."

    return f"User '{name}' already exist or phone number not valid.\n"\
        "The phone number should look like +380123456789"


@input_error
def change(data: str) -> str:

    name, phone = data.split()
    phone = re.search(r"\+380\d{9}", phone)

    if ADDRESS_BOOK.get_contact(name) and phone:

        new_phone = Phone()
        new_phone.mobile_phone = phone.group()
        name = Name(name)
        record = Record(name)
        record.add_phone(new_phone)
        ADDRESS_BOOK.add_record(record)

        return f"User '{name.value}' changed on address book."

    return f"User '{name}' not found on phone book or phone number not valid.\n"\
        "The phone number should look like +380123456789"


@input_error
def phone(data: str) -> str:

    name = data
    record = ADDRESS_BOOK.get_contact(name)
    message = "|{:^10}|{:^13}|\n".format("User", "Phone")
    message += "-" * 26 + "\n"

    if record:
        for phone in record.phones:
            message += "|{:^10}|{:<13}|".format(name, phone.mobile_phone)

    return message


@input_error
def show_all() -> str:

    message = "|{:^10}|{:^13}|\n".format("User", "Phone")
    message += "-" * 26 + "\n"
    list_contacts = ADDRESS_BOOK.list_contacts()
    
    for name, record in list_contacts.items():

      for phone in record.phones:
        message += "|{:^10}|{:<13}|\n".format(name, phone.mobile_phone)

    return message
