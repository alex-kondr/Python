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

    def execute(self, name, type_field, value):
        new_field = Field.list_type_fields[type_field](value)
        record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
        record.add_field(new_field)
        ADDRESS_BOOK.add_record(record)

        return f"The contact type {type_field} value {value} is added to "\
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

    def execute(self, __, name, *_):
        record = ADDRESS_BOOK.get_contact(name.title())

        if not record:
            return f"The contact {name.title()} not found"

        return record.days_to_birthday()


class GoodBye(Close, Action): ...


class Exit(Close, Action): ...


class ShowContact(Action):

    def execute(self, name, *_):

        record = ADDRESS_BOOK.get_contact(name)

        if not record:
            return f"The contact {name.title()} not found"

        address_book = AddressBook()
        address_book.add_record(record)
        table = TableForAddresBook(address_book)        

        return table.header() + table.table()

class ShowAll(Action):

    def execute(self, *_):
        table = TableForAddresBook(ADDRESS_BOOK)

        return table.header() + table.table()


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
