from abc import ABC, abstractmethod
from termcolor import colored

from fields import Record


class Table(ABC):

    @abstractmethod
    def header(): ...

    @abstractmethod
    def table(): ...


class TableForRecord(Table):

    def __init__(self, record: Record) -> None:
        self.record = record
        self.headers = record.types_of_fields()
        self.len_cells = self.record.list_len_cells()
        self.dividing_line = ""

    def header(self):
        columns = "\n"

        for i, head in enumerate(self.headers):
            columns += f"| {head:^{self.len_cells[i]}} "

        columns += "|"
        self.dividing_line = "\n|" + "-" * (len(columns) - 3) + "|"

        return self.dividing_line + columns + self.dividing_line

    def table(self):

        table = ""
        all_table = [list_fields.list_values() for list_fields in self.record.values()]
        max_len_table = len(max(all_table, key=lambda table: len(table)))

        for i in range(max_len_table):
            table += "\n"

            for j, item in enumerate(all_table):

                item = item[i] if i < len(item) else ""
                table += f"| {item:^{self.len_cells[j]}} "

            table += "|"

        return table + self.dividing_line

    



# name = Name("alex")
# record = Record(name)
# phone = Phone("+380121234556")
# phone1 = Phone("+380121234557")
# birth = Birthday("01.01.1988")
# record.add_field(birth)
# record.add_field(phone)
# record.add_field(phone1)

# email = Email("alex_kondr@outlook.com")
# record.add_field(email)

# # print(record.types_of_fields())
# # header = Header(record)
# # print(header.create_line())
# table = TableForRecord(record)
# line = table.header() + table.table()

# print(line)
