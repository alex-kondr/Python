from abc import ABC, abstractmethod
from pathlib import Path
import pickle, re
from termcolor import colored

from address_book import AddressBook
from fields import Field, Name, Record
from input_error import input_error


FILE = Path("address_book.bin")


class Action(ABC):

    list_actions = {}

    def __init_subclass__(cls) -> None:

        cls_name = re.findall(r"[A-Z][a-z]+", cls.__name__)
        
        Action.list_actions.update(
            {" ".join(cls_name).lower(): cls}
        )
    
    @abstractmethod    
    def execute(self, name: str, type_field: str, value: str) -> str: ...


class Add(Action):

    @input_error
    def execute(self, name: str, type_field: str, value: str) -> str:

        find = Find()
        find = find.execute("", value, "")

        if isinstance(find, AddressBook) and find.get_contact(name):
            return colored(f"The contact '{name}' already have value '{value}'", "magenta")

        new_field = Field.list_type_fields[type_field](value)
        record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
        record.add_field(new_field)
        ADDRESS_BOOK.add_record(record)

        return colored(f"The contact type '{type_field}' value '{value}' is added to "\
            f"the user '{name}' in the phone book.", "green")


class Birthday(Action):

    @input_error
    def execute(self, __, name: str, *_) -> str:
        record = ADDRESS_BOOK.get_contact(name.title())

        if not record:
            return colored(f"The contact {name.title()} not found", "magenta")

        return colored(f"The contact '{name.title()}' will be celebrating a birthday"
                       f" through {record.days_to_birthday()} days", "green")


class Birthdays(Action):

    @input_error
    def execute(self, __, days: str, *_) -> AddressBook|str:
        address_book = AddressBook()

        for record in ADDRESS_BOOK.data.values():
            if record.days_to_birthday() < int(days):
                address_book.add_record(record)

        if not address_book.data:
            return colored("There are no contacts who celebrate"
                f" a birthday in the following '{days}' days", "magenta")

        return address_book


class Change(Action):

    @input_error
    def execute(self, name: str, type_field: str, value: str) -> str:
        record = ADDRESS_BOOK.get_contact(name)

        if not record:
            return colored(f"The contact {name} not found", "magenta")

        values = record.get_values(type_field.title())

        for i, val in enumerate(values):
            print(colored(f"\n{i}: {val}", "green"))

        number = int(
            input(colored("Select the number in the order you want to change: ", "yellow")))

        record.change_field(type_field.title(), number, value)

        return colored(f"User '{name}' changed {type_field} on address book.", "green")


class Clear(Action):
    
    @input_error
    def execute(self, *_) -> str:
        ADDRESS_BOOK.clear_address_book()

        return colored("The address book is cleared", "green")


class Close(Action):

    @input_error
    def execute(self, *_):
        ADDRESS_BOOK.save_data(FILE)
        print(colored("Good bye.", "cyan"))
        quit()


class Del(Action):

    @input_error
    def execute(self, name: str, type_field: str, *_) -> str:
        record = ADDRESS_BOOK.get_contact(name)

        if not record:
            return colored(f"The contact {name} not found", "magenta")

        values = record.get_values(type_field.title())

        for i, val in enumerate(values):
            print(colored(f"\n{i}: {val}", "green"))

        number = int(
            input(colored("Select the number in the order you want to change: ", "yellow")))

        field = record.remove_field(number, type_field.title())

        return colored(f"\nIn user '{name}' deleted {type_field} '{field.value}' on address book.", "green") #type: ignore


class Exit(Close, Action): ...


class Find(Action):

    @input_error
    def execute(self, __, data: str, *_) -> AddressBook|str:
        address_book = AddressBook()
        
        for name, record in ADDRESS_BOOK.data.items():
            for list_fields in record.data.values():
                for value in list_fields.list_values():
                    if (data.lower() in value.lower() or
                        data.lower() in name.lower()):

                        address_book.add_record(record)

        if not address_book.data:
            return colored(f"There is no contact with such data '{data}' in the addres book", "magenta")

        return address_book


class GoodBye(Close, Action): ...


class Help(Action):

    @input_error
    def execute(self, *_) -> str:
        message = "\nThis bot following commands for the address book:\n\n"

        for i, action in enumerate(Action.list_actions):
            message += f"{i}: {action}"

        message += "\nAlso, each contact have such fields:\n\n"

        for i, field in enumerate(Field.list_type_fields):
            message += f"{i}: {field}\n"

        return colored(message, "cyan")


class RemoveContact(Action):

    @input_error
    def execute(self, name: str, *_) -> str:
        ADDRESS_BOOK.remove_contact(name)

        return colored(f"The contact '{name}' has been deleted", "green")


class ShowAll(Action):

    @input_error
    def execute(self, *_) -> AddressBook:
        return ADDRESS_BOOK


class ShowContact(Action):

    @input_error
    def execute(self, name: str, *_) -> AddressBook|str:

        record = ADDRESS_BOOK.get_contact(name)

        if not record:
            return f"The contact {name.title()} not found"

        address_book = AddressBook()
        address_book.add_record(record)      

        return address_book


def load_data(file) -> AddressBook:

    if not file.exists():
        return AddressBook()

    with open(file, "rb") as fh:
        return pickle.load(fh)


ADDRESS_BOOK = load_data(FILE)
