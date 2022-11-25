from pathlib import Path
import pickle

from address_book import AddressBook
from fields import Birthday, Name, Phone, Record
from input_error import input_error


FILE = Path("address_book.bin")


@input_error
def add(data: str) -> str:
    name, phone = data.split()
    new_phone = Phone(phone)
    record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
    record.add_phone(new_phone)
    ADDRESS_BOOK.add_record(record)

    return f"The mobile phone {phone} is added to "\
        f"the user '{name}' in the phone book."


@input_error
def add_birthday(data: str) -> str:
    name, birthday = data.split()
    record = ADDRESS_BOOK.data.get(name)

    if not record:
        return f"User '{name}' not found on phone book."

    record.birthday = Birthday(birthday)

    return f"\nBirthday added to user '{name}'"


@input_error
def change_phone(name: str) -> str:
    record = ADDRESS_BOOK.data.get(name)

    if not record:
        raise ValueError(f"User '{name}' not found on phone book.")

    print("\nWhat number do you want change?")
    print(get_contact(name))
    number = int(
        input("Select the number in the order you want to change: "))
    mobile_phone = input("\nEnter new mobile number: ")
    record.change_phone(number, mobile_phone)

    return f"User '{name}' changed mobile phone on address book."


@input_error
def days_to_birthday(name: str) -> int:
    record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
    return record.days_to_birthday()


def find_contacts(data: str):
    contacts = AddressBook()
    
    for name, record in ADDRESS_BOOK.data.items():
        if data in name or data in record.list_phones():
            contacts.update({name: record})
            
    return contacts


@input_error
def get_contact(name: str) -> AddressBook:
    data = AddressBook()
    data.update({name: ADDRESS_BOOK.data.get(name)})

    if not ADDRESS_BOOK.data.get(name):
        raise ValueError(f"User '{name}' not found on phone book.")

    return data


def load_data(file, default=AddressBook()) -> AddressBook:

    if not file.exists():
        return default

    with open(file, "rb") as fh:
        return pickle.load(fh)    


@input_error
def remove_phone(name: str) -> str:
    record = ADDRESS_BOOK.data.get(name)

    if not record:
        raise ValueError(
            f"User '{name}' not found on phone book or phone number not valid.\n")

    print("\nWhat number do you want delete?")
    print(get_contact(name))

    number = int(
        input("Select the number in the order you want to delete: "))
    phone = record.remove_phone(number)

    if not record:
        pass

    return f"\nIn user '{name}' deleted mobile phone '{phone.value}' on address book."


def save_data(data, file):

    with open(file, "wb") as fh:
        pickle.dump(data, fh)


@input_error
def show_all(_) -> AddressBook:
    data = AddressBook()
    ADDRESS_BOOK.position_in_dict = 0
    input_n = input("How many records to show at once. Press enter to show all: ")
    ADDRESS_BOOK.N = int(input_n) if input_n else 0    # type: ignore
    
    for data in ADDRESS_BOOK:
        if ADDRESS_BOOK.position_in_dict != len(ADDRESS_BOOK):
            
            print(data)
            input("Press enter to download the next part ")
    
    return data
    

ADDRESS_BOOK = load_data(FILE)
