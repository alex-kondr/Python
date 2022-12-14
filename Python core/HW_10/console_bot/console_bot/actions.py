import re
from address_book import AddressBook, Name, Phone, Record
from input_error import input_error


ADDRESS_BOOK = AddressBook()


@input_error
def add(data: str) -> str:

    name, phone = data.split()
    phone = re.search(r"\+380\d{9}", phone)

    if ADDRESS_BOOK.get_contact(name) or not phone:
        return f"User '{name}' already exist or phone number not valid.\n"\
                "The phone number should look like +380123456789"
        
    new_phone = Phone()
    new_phone.mobile_phone = phone.group()
    name = Name(name)
    record = Record(name)
    record.add_phone(new_phone)
    ADDRESS_BOOK.add_record(record)
    
    return f"User '{name.value}' added to phone book."    


@input_error
def change(name: str) -> str:

    record = ADDRESS_BOOK.get_contact(name)    

    if not record:
        return f"User '{name}' not found on phone book."   

    message = "\nWhat number do you want change\n"
    message += "\n|{:^10}|{:^13}|\n".format("Number", "Phone")
    message += "-" * 26 + "\n"

    for i, phone in enumerate(record.phones):
        message += "|{:^10}|{:<13}|\n".format(i+1, phone.mobile_phone)
        print(message)

    number = int(input("Select the number in the order you want to change: ")) - 1
    mobile_phone = input("\nEnter new mobile number: ")
    mobile_phone = re.search(r"\+380\d{9}", mobile_phone)

    if not mobile_phone:
        return f"Phone number is not valid.\n"\
            "The phone number should look like + 380123456789"

    record.change_phone(number, mobile_phone.group())

    return f"User '{name}' changed mobile phone on address book."    


@input_error
def phone(name: str) -> str:

    record = ADDRESS_BOOK.get_contact(name)
    message = "|{:^10}|{:^13}|\n".format("User", "Phone")
    message += "-" * 26 + "\n"

    if record:
        for phone in record.phones:
            message += "|{:^10}|{:<13}|".format(name, phone.mobile_phone)

    return message


@input_error
def remove_phone(name: str) -> str:

    record = ADDRESS_BOOK.get_contact(name)

    if  not record:
        return f"User '{name}' not found on phone book or phone number not valid.\n"

    message = "\nWhat number do you want delete?\n"
    message += "\n|{:^10}|{:^13}|\n".format("Number", "Phone")
    message += "-" * 26 + "\n"

    for i, phone in enumerate(record.phones):
        message += "|{:^10}|{:<13}|\n".format(i+1, phone.mobile_phone)
        print(message)

    number = int(input("Select the number in the order you want to delete: ")) - 1
    phone = record.remove_phone(number)

    return f"\nIn user '{name}' deleted mobile phone '{phone.mobile_phone}' on address book."
    

def show_all() -> str:

    message = "\n|{:^10}|{:^13}|\n".format("User", "Phone")
    message += "-" * 26 + "\n"
    list_contacts = ADDRESS_BOOK.list_contacts()
    
    for name, record in list_contacts.items():

        for phone in record.phones:
            message += "|{:^10}|{:<13}|\n".format(name, phone.mobile_phone)

    return message
