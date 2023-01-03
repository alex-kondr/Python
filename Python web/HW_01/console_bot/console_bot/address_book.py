from collections import UserDict
import pickle
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

        return table.header() + table.table()

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


    # def max_column(self):
    #     max_len = 0
    #     columns = []
    #     for record in self.data.values():
    #         fields = [field for field in record]
            
    #         if len(fields) > max_len:
    #             columns = fields
    #             max_len = len(fields)
        
    #     return columns


# class TabularInterface:

#     def __init__(self, address_book):

        
#         self.len_cells = max([max(record.list_len_cells()) for record in address_book.data.values()])
#         self.template = "\n|{:^3}|{:^13}|{:^3}|{:^13}|{:^3}| {:^{len_cells}} |"
#         headers = ["№", "User", "№", "Type", "№", "Value"]
#         self.header = self.template.format(*headers, len_cells=self.len_cells)
#         self.dividing_line = "\n|" + "-" * (len(self.header) - 3) + "|"

#         self.output_table = self.dividing_line

#     def dict_in_table(self):
#         output_table = self.dividing_line + self.header + self.dividing_line

#         for i, (name, record) in enumerate(address_book.items()):
#             for j, (type_field, fields) in enumerate(record.data.items()):
#                 for k, field in enumerate(fields):

#                     output_table += self.template.format(
#                         i, name, j, type_field, k, field.value, len_cells=self.len_cells)

#                     i, j, name, type_field = "", "", "", ""
            
#             output_table += self.dividing_line

#         return output_table
        

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

# address_book = AddressBook()
# address_book.add_record(record)

# name1 = Name("Anny")
# record1 = Record(name1)
# phone2 = Phone("+380121234556")
# phone3 = Phone("+380121234557")
# birth1 = Birthday("01.01.1988")
# record1.add_field(birth1)
# record1.add_field(phone2)
# record1.add_field(phone3)

# email1 = Email("alex_kondr@outlook.com")
# record1.add_field(email1)

# # address_book = AddressBook()
# address_book.add_record(record1)




# print(address_book)

# # print(record.types_of_fields())
# # header = Header(record)
# # print(header.create_line())
# table = TableForRecord(record)
# line = table.header() + table.table()

# print(line)
