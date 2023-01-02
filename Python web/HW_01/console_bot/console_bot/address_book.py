from collections import UserDict
from fields import *


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()
        self.position_in_dict = 0
        self.N = 0        

    def __iter__(self):
        return self

    def __next__(self):
        data = AddressBook()

        if self.position_in_dict >= len(self.data):
            raise StopIteration

        for n, (name, record) in enumerate(self.data.items()):
            if n >= self.position_in_dict and (len(data) < self.N or not self.N):

                data.update({name: record})
                self.position_in_dict += 1

        return data

    def __str__(self):

        headers = ["№", "User", "№", "Type", "№", "Value"]
        tabular = TabularInterface(headers, self)

        return tabular.dict_in_table(self.data)

    def add_record(self, record):
        self.data.update({record.name.value: record})

    def max_column(self):
        max_len = 0
        columns = []
        for record in self.data.values():
            fields = [field for field in record]
            
            if len(fields) > max_len:
                columns = fields
                max_len = len(fields)
        
        return columns



# class TabularInterface:

#     def __init__(self, headers: list):
#         self.columns = "\n" + "|{:^3}|{:^13}" * (len(headers) // 2) + "|"
#         self.header = self.columns.format(*headers)
#         self.header += "\n|" + "-" * (18 * (len(headers) // 2) - 1) + "|"

#     def dict_in_table(self, address_book):
#         output_table = self.header

#         for i, (name, record) in enumerate(address_book.items()):
#             for j, (type_field, fields) in enumerate(record.data.items()):
#                 for k, field in enumerate(fields):

#                     output_table += self.columns.format(
#                         i, name, j, type_field, k, field.value)

#                     i, j, name, type_field = "", "", "", ""

#         return output_table

class TabularInterface:

    def __init__(self, headers: list, address_book):

        self.len_cells = max([max(record.list_len_cells()) for record in address_book.data.values()])
        # print([max(record.list_len_cells()) for record in address_book.data.values()]


)
        # for i in len(len_cells):


        # for record in address_book.value():
        #     for 


        self.columns = "\n" + "|{:^3}|{:^{len_cells}}" * (len(headers) // 2) + "|"
        self.header = self.columns.format(*headers, len_cells=self.len_cells)
        self.dividing_line = "\n|" + "-" * (len(self.header) - 3) + "|"

    # def header(self, headers: list):
    #     table = "\n"

    #     for header in headers:
    #         table += f"|{'№'}"

    def dict_in_table(self, address_book):
        output_table = self.header + self.dividing_line

        for i, (name, record) in enumerate(address_book.items()):
            for j, (type_field, fields) in enumerate(record.data.items()):
                for k, field in enumerate(fields):

                    output_table += self.columns.format(
                        i, name, j, type_field, k, field.value, len_cells=self.len_cells)

                    i, j, name, type_field = "", "", "", ""

        return output_table
        

name = Name("alex")
record = Record(name)
phone = Phone("+380121234556")
phone1 = Phone("+380121234557")
birth = Birthday("01.01.1988")
record.add_field(birth)
record.add_field(phone)
record.add_field(phone1)

email = Email("alex_kondr@outlook.com")
record.add_field(email)

address_book = AddressBook()
address_book.add_record(record)

name1 = Name("Anny")
record1 = Record(name1)
phone2 = Phone("+380121234556")
phone3 = Phone("+380121234557")
birth1 = Birthday("01.01.1988")
record1.add_field(birth1)
record1.add_field(phone2)
record1.add_field(phone3)

email1 = Email("alex_kondr@outlook.com")
record1.add_field(email1)

# address_book = AddressBook()
address_book.add_record(record1)




print(address_book)

# # print(record.types_of_fields())
# # header = Header(record)
# # print(header.create_line())
# table = TableForRecord(record)
# line = table.header() + table.table()

# print(line)
