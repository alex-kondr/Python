from pathlib import Path
import pickle

from address_book import AddressBook
from fields import Address, Birthday, Email, Name, Phone, Record
from input_error import input_error


FILE = Path("address_book.bin")

TYPE_FIELD = {
    "address": Address,
    "email": Email,
    "phone": Phone
}


@input_error
def add(data: str) -> str:
    name, type_field, value = data.split()
    new_field = TYPE_FIELD[type_field](value)
    record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
    record.add_field(new_field)
    ADDRESS_BOOK.add_record(record)

    return f"The contact type {type_field} value {value} is added to "\
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
def change_field(name: str) -> str:
    record = ADDRESS_BOOK.data.get(name)

    if not record:
        raise ValueError(f"User '{name}' not found on address book.")

    type_field = input("Enter type field: ").title()

    name_type_field = name + " " + type_field
    
    print(get_contact_for_type(name_type_field))
    
    number = int(
        input("Select the number in the order you want to change: "))
    new_field = input("\nEnter new field: ")
    record.change_field(type_field, number, new_field)

    return f"User '{name}' changed {type_field} on address book."


@input_error
def days_to_birthday(name: str) -> int:
    record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
    return record.days_to_birthday()


def find_contacts(data: str):
    contacts = AddressBook()
    
    for name, record in ADDRESS_BOOK.data.items():
        for fields in record.fields.values():
            values = [field.value for field in fields if data in field.value]

            if values or data in name:
                contacts.update({name: record})

    return contacts


@input_error
def get_contact_for_type(name_type_field: str) -> AddressBook:
    name, type_field = name_type_field.split()
    data = AddressBook()
    record = ADDRESS_BOOK.data.get(name)
    data_record = Record(Name(name))

    if not record:
        raise ValueError(f"User '{name}' not found on phone book.")

    for field in record.fields[type_field.title()]:
        data_record.add_field(field)

    data.update({name: data_record})

    return data


def load_data(file, default=AddressBook()) -> AddressBook:

    if not file.exists():
        return default

    with open(file, "rb") as fh:
        return pickle.load(fh)    


@input_error
def remove_field(name_type_field: str) -> str:
    name, type_field = name_type_field.split()
    record = ADDRESS_BOOK.data.get(name)

    if not record:
        raise ValueError(
            f"User '{name}' not found on phone book or phone number not valid.\n")

    print("\nWhat number do you want delete?")
    print(get_contact_for_type(name_type_field))

    number = int(
        input("Select the number in the order you want to delete: "))
    field = record.remove_field(number, type_field.title())

    return f"\nIn user '{name}' deleted {type_field} '{field.value}' on address book."


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

# add("Bob phone +380123456789")
# add("Bob phone +380509228157")
# add("Bob email 456")
# add("Bob email 789")
# add("Bob email 789")
# add("Bob phone +380123456789")
# add("Bob phone +380509228157")
# add("Bob email 456")
# add("Bob email 789")
# add("Bob email 789")
# add("alex phone +380123456789")
# add("alex phone +380509228157")
# add("alex email 456")
# add("alex1 email 789")
# add("alex email 789")

# record = ADDRESS_BOOK.data["Bob"]
# fields = record.fields["Phone"]

# a = [field.value for field in fields]
# print(a)

# headers = ["№", "User", "№", "Type", "№", "Value"]
# tabular = interface.TabularInterface(headers)
# print(tabular.dict_in_table(ADDRESS_BOOK.data))

# print(ADDRESS_BOOK)
# phone = Phone("+380509228157")
# record = Record("111")
# record.add_contact(phone)

# phone = Phone("+380509228158")
# record.add_contact(phone)

# email = Email("456")
# record.add_contact(email)

# print(record.list_fields())
