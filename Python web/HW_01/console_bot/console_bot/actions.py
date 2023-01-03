from abc import ABC, abstractmethod
from pathlib import Path
import pickle
import re

from address_book import AddressBook
from fields import Field, Name, Record
from input_error import input_error
from interface import TableForAddresBook


FILE = Path("address_book.bin")


class Action(ABC):

    list_actions = {}

    def __init_subclass__(cls) -> None:

        cls_name = re.findall(r"[A-Z][a-z]+", cls.__name__)
        
        Action.list_actions.update(
            {" ".join(cls_name).lower(): cls}
        )

    @abstractmethod
    def execute(self, name, type_field, value) -> str: ...


class Add(Action):

    def execute(self, name, type_field, value) -> str:

        find = Find()
        find = find.execute("", value, "")

        if isinstance(find, AddressBook) and find.get_contact(name):
            return f"The contact '{name}' already have value '{value}'"

        new_field = Field.list_type_fields[type_field](value)
        record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
        record.add_field(new_field)
        ADDRESS_BOOK.add_record(record)

        return f"The contact type '{type_field}' value '{value}' is added to "\
            f"the user '{name}' in the phone book."


class Change(Action):

    def execute(self, name, type_field, value) -> str:
        record = ADDRESS_BOOK.get_contact(name)

        if not record:
            return f"The contact {name} not found"

        values = record.get_values(type_field.title())

        for i, val in enumerate(values):
            print(f"{i}: {val}")

        number = int(
            input("Select the number in the order you want to change: "))

        record.change_field(type_field.title(), number, value)

        return f"User '{name}' changed {type_field} on address book."


class Close(Action):

    def execute(self, *_):
        ADDRESS_BOOK.save_data(FILE)
        print("Good bye.")
        quit()

class Clear(Action):

    def execute(self, name, type_field, value) -> str:
        ADDRESS_BOOK.clear_address_book()

        return "The address book is cleared"


class Del(Action):

    def execute(self, name, type_field, *_) -> str:
        record = ADDRESS_BOOK.get_contact(name)

        if not record:
            return f"The contact {name} not found"

        values = record.get_values(type_field.title())

        for i, val in enumerate(values):
            print(f"\n{i}: {val}\n")

        number = int(
            input("Select the number in the order you want to change: "))

        field = record.remove_field(number, type_field.title())

        return f"\nIn user '{name}' deleted {type_field} '{field.value}' on address book." #type: ignore


class Birthday(Action):

    def execute(self, __, name, *_) -> str:
        record = ADDRESS_BOOK.get_contact(name.title())

        if not record:
            return f"The contact {name.title()} not found"

        return f"The contact '{name.title()}' will be celebrating a birthday through {record.days_to_birthday()} days"


class Find(Action):

    def execute(self, __, data: str, *_) -> AddressBook|str:
        address_book = AddressBook()
        
        for name, record in ADDRESS_BOOK.data.items():
            for list_fields in record.data.values():
                for value in list_fields.list_values():
                    if (data.lower() in value.lower() or
                        data.lower() in name.lower()):

                        address_book.add_record(record)

        if not address_book.data:
            return f"There is no contact with such data '{data}' in the addres book"

        return address_book


class GoodBye(Close, Action): ...


class Exit(Close, Action): ...


class RemoveContact(Action):

    def execute(self, name, *_) -> str:
        ADDRESS_BOOK.remove_contact(name)

        return f"The contact '{name}' has been deleted"


class ShowAll(Action):

    def execute(self, *_) -> AddressBook:
        return ADDRESS_BOOK


class ShowContact(Action):

    def execute(self, name, *_) -> AddressBook|str:

        record = ADDRESS_BOOK.get_contact(name)

        if not record:
            return f"The contact {name.title()} not found"

        address_book = AddressBook()
        address_book.add_record(record)      

        return address_book


def load_data(file, default=AddressBook()) -> AddressBook:

    if not file.exists():
        return default

    with open(file, "rb") as fh:
        return pickle.load(fh)


ADDRESS_BOOK = load_data(FILE)

# command = "add".lower()
# type_field = "phone".lower()
# name = "alex"
# value = "+380509228157"

# action = Action.list_actions.get(command)()
# # print(action)
# print(action.execute(name, type_field, value))
# print(ADDRESS_BOOK.data)
