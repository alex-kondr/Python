from collections import UserDict
import pickle

from termcolor import colored

from fields import Record
from interface import TableForAddresBook


class AddressBook(UserDict):

    # def __init__(self) -> None:
    #     super().__init__()
    #     self.position_in_dict = 0
    #     self.N = 0        

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     data = AddressBook()

    #     if self.position_in_dict >= len(self.data):
    #         raise StopIteration

    #     for n, (name, record) in enumerate(self.data.items()):
    #         if n >= self.position_in_dict and (len(data) < self.N or not self.N):

    #             data.update({name: record})
    #             self.position_in_dict += 1

    #     return data

    def __str__(self) -> str:

        if not self.data:
            return "Address book is empty"

        table = TableForAddresBook(self)

        return colored(table.header() + table.table(), "green")

    def add_record(self, record) -> None:
        self.data.update({record.name.value: record})

    def clear_address_book(self) -> None:
        self.data.clear()

    def get_contact(self, name: str) -> Record|None:
        return self.data.get(name)

    def remove_contact(self, name: str) -> None:
        self.data.pop(name)

    def save_data(self, file) -> None:

        with open(file, "wb") as fh:
            pickle.dump(self, fh)
