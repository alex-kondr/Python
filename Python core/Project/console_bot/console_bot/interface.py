class TabularInterface:

    def __init__(self, header: list):
        self.columns = "\n" + "|{:^3}|{:^13}" * (len(header) // 2) + "|\n"
        self.header = self.columns.format(*header)
        self.header += "|" + "-" * 53 + "|\n"


    def dict_in_table(self, address_book):
        output_table = ""

        for i, (name, record) in enumerate(address_book.items()):
            for j, (type, fields) in enumerate(record.items()):
                for k, field in enumerate(fields):
                    pass

        return output_table

    # def tamplate(self, data: list):




        


header = ["№", "User", "№", "Type", "№", "Value"]
tabular = TabularInterface(header)
print(tabular.dict_in_table(""))