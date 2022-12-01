from collections import UserDict


class AddressBook(UserDict):

    def __str__(self):
        message = "\n|{:^3}|{:^10}|{:^3}|{:^13}|\n".format(
            "№", "User", "№", "Phone")
        message += "|" + "-" * 32 + "|\n"
        i = 0

        for name, record in self.data.items():
            if not record.phones:
                i -= 1
            else:
                message += "|{:^3}|{:^10}|{:^13}".format(
                    i, name, record.list_phones())
            
            i += 1
        
        return message

    def add_record(self, record):
        self.data.update({record.name.value: record})

    def iterator(self, N: int):
        i = 0
        data = AddressBook()
        
        for n, (name, record) in enumerate(self.data.items()):
            data.update({name: record})
            i += 1

            if i == N or n == len(self.data) - 1:
                yield data
                data.clear()
                i = 0
