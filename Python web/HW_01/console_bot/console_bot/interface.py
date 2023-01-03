from abc import ABC, abstractmethod
from termcolor import colored


class Table(ABC):

    @abstractmethod
    def header() -> str: ...

    @abstractmethod
    def table() -> str: ...


class TableForAddresBook(Table):

    def __init__(self, address_book) -> None:

        self.address_book = address_book
        self.max_cell_len = max([max(record.list_len_cells())
                             for record in self.address_book.data.values()])
        self.template = "\n|{:^3}|{:^13}|{:^3}|{:^13}|{:^3}| {:^{max_cell_len}} |"
        self.dividing_line = ""
        
    
    def header(self) -> str:

        headers = ["№", "User", "№", "Type", "№", "Value"]
        header = self.template.format(
            *headers, max_cell_len=self.max_cell_len)
        self.dividing_line = "\n|" + "-" * (len(header) - 3) + "|"

        return self.dividing_line + header + self.dividing_line

    def table(self) -> str:

        table = ""

        for i, (name, record) in enumerate(self.address_book.data.items()):
            for j, (type_field, fields) in enumerate(record.data.items()):
                for k, field in enumerate(fields):

                    table += self.template.format(
                        i, name, j, type_field, k, field.value, max_cell_len=self.max_cell_len)

                    i, j, name, type_field = "", "", "", ""

            table += self.dividing_line

        return table

    



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
