from collections import UserDict


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
        tabular = TabularInterface(headers)

        return tabular.dict_in_table(self.data)

    def add_record(self, record):
        self.data.update({record.name.value: record})


class Note(UserDict):
    
    def add_note(self, short, long):
        self.data.update({short: long})


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
