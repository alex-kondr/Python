from abc import ABC, abstractmethod
from pathlib import Path
import pickle

from address_book import AddressBook
from fields import Field, Address, Birthday, Email, Name, Phone, Record
from input_error import input_error
from interface import Header, TableForContact


FILE = Path("address_book.bin")


class Action(ABC):

    list_actions = {}

    def __init_subclass__(cls) -> None:
        Action.list_actions.update(
            {cls.__name__.lower(): cls}
        )

    @abstractmethod
    def execute(): ...


class Add(Action):

    def execute(self, name, type_field, value):
        new_field = Field.list_type_fields[type_field](value)
        record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
        record.add_field(new_field)
        ADDRESS_BOOK.add_record(record)

        return f"The contact type {type_field} value {value} is added to "\
            f"the user '{name}' in the phone book."


class Change(Action): ...


class Del(Action): ...


class Show(Action):

    def execute(self, name, *_):
        record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
        table = Header(record).create_table()
        table += TableForContact(record).create_table()

        return table

class ShowAll(Action):

    def execute(self, *_):
        # record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
        # table = Header(Record(Name(""))).create_table()
        # for name, record in ADDRESS_BOOK.data.items():

        records = [record for record in ADDRESS_BOOK.data.values()]
        # print(all_type_fields)
        max_len = max(records, key=lambda record: len(record.types_of_fields()))
        # print(max_len)
        # table += TableForContact(record).create_table()

        # return table


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
