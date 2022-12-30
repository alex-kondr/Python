from abc import ABC, abstractmethod
from termcolor import colored

from fields import *


class OneLine(ABC):

    @abstractmethod
    def print_line(self):
        pass


class Header(OneLine):

    def __init__(self, record: Record) -> None:
        self.types_of_fields = record.types_of_fields()

    def print_line(self):
        
        header = "\n|" + "-" * (18 * (len(self.types_of_fields) // 2) - 1) + "|"
        columns = "\n" + "|{:^3}|{:^13}" * (len(self.types_of_fields) // 2)  + "|"
        header += columns.format(*self.types_of_fields)
        header += "\n|" + "-" * (18 * (len(self.types_of_fields) // 2) - 1) + "|"

        return header


name = Name("alex")
record = Record(name)
phone = Phone("+380121234556")
birth = Birthday("01.01")
record.add_field(birth)
record.add_field(phone)


# print(record.types_of_fields())
header = Header(record)
print(header.print_line())



class LineOfField(OneLine):

    def __init__(self, record: Record) -> None:
        self.record = record

    def print_line(self):
        pass




class TabularInterface:

    def __init__(self, headers: list):
        self.columns = "\n" + "|{:^3}|{:^13}" * (len(headers) // 2) + "|"
        self.header = self.columns.format(*headers)
        self.header += "\n|" + "-" * (18 * (len(headers) // 2) - 1) + "|"

    def dict_in_table(self, address_book):
        output_table = self.header

        for i, (name, record) in enumerate(address_book.items()):
            for j, (type_field, fields) in enumerate(record.fields.items()):
                for k, field in enumerate(fields):

                    output_table += self.columns.format(
                        i, name, j, type_field, k, field.value)

                    i, j, name, type_field = "", "", "", ""

        return output_table


def header_func() -> str:

    header = "\n|" + "-" * 117 + "|"
    headers = ["Name", "Phone", "Birthday", "Email", "Tags", "Notes"]
    columns = "\n|{:^15}|{:^15}|{:^12}|{:^25}|{:^15}|{:^30}|"
    header += columns.format(*headers)
    header += "\n|" + "-" * 117 + "|"
    header = colored(f"{header}", "blue")

    return header


def line_func(record: Record) -> str:

    line = ""
    columns = "\n|{:^15}|{:^15}|{:^12}|{:^25}|{:^15}|{:^30}|"

    name = record.name.value.title()
    name_table = [name[i:i+13] for i in range(0, len(name), 13)]

    phone_table = [phone.value for phone in record.phones]

    birthday = record.birthday.value.strftime(
        "%d.%m.%Y") if record.birthday else ""
    birthday_table = [birthday]

    email_table = []

    for email in record.emails:
        for i in range(0, len(email.value), 23):
            email_table.append(email.value[i:i+23])

    tag = record.tag.value if record.tag else ""
    tag_table = []
    temp = ""
    tag_i = ""

    for tag_i in tag:

        if len(temp + tag_i) < 13:
            temp += " " + tag_i

        else:
            tag_table.append(temp)
            temp = tag_i

    tag_table.append(temp)

    note = record.note.value if record.note else " "
    note_table = [note[i:i+28] for i in range(0, len(note), 28)]

    all_table = [name_table, phone_table, birthday_table,
                 email_table, tag_table, note_table]
    max_len_table = len(max(all_table, key=lambda table: len(table)))

    for i in range(max_len_table):
        cells = []

        for table in all_table:

            table = table[i] if i < len(table) else ""
            cells.append(table)

        line += columns.format(*cells)

    line += "\n|" + "-" * 117 + "|"

    return line
