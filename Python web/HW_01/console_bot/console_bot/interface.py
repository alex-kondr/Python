from abc import ABC, abstractmethod
from termcolor import colored

from fields import *


class Table(ABC):

    @abstractmethod
    def create_table(self):
        pass


class Header(Table):

    def __init__(self, record: Record) -> None:
        self.types_of_fields = record.types_of_fields()

    def create_table(self):
        
        header = "\n|" + "-" * (18 * (len(self.types_of_fields) // 2) - 1) + "|"
        columns = "\n" + "|{:^3}|{:^13}" * (len(self.types_of_fields) // 2)  + "|"
        header += columns.format(*self.types_of_fields)
        header += "\n|" + "-" * (18 * (len(self.types_of_fields) // 2) - 1) + "|"

        return header


class TableForContact(Table):

    def __init__(self, record: Record) -> None:
        self.record = record

    def create_table(self):
        line = ""
        columns = "\n" + "|{:^3}|{:^13}" * (len(self.record.types_of_fields()) // 2) + "|"

        all_table = [list_fields.list_values() for list_fields in self.record.data.values()]
        max_len_table = len(max(all_table, key=lambda table: len(table)))

        for i in range(max_len_table):
            cells = []

            for table in all_table:

                table = table[i] if i < len(table) else ""
                j = i if i < len(table) else ""
                cells += [j, table]

            line += columns.format(*cells)

        line += "\n|" + "-" * (18 * (len(self.record.types_of_fields()) // 2) - 1) + "|"

        return line


# name = Name("alex")
# record = Record(name)
# phone = Phone("+380121234556")
# phone1 = Phone("+380121234557")
# birth = Birthday("01.01")
# record.add_field(birth)
# record.add_field(phone)
# record.add_field(phone1)

# print(record.types_of_fields())
# header = Header(record)
# print(header.create_line())
# line_of_field = LineOfField(record)
# print(line_of_field.create_line())
