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
        message = "\n|{:^3}|{:^10}|{:^3}|{:^13}|\n".format(
            "№", "User", "№", "Phone")
        message += "|" + "-" * 32 + "|\n"
        i = 0

        for name, record in self.data.items():
            if record.phones:
                message += "|{:^3}|{:^10}|{:^13}".format(
                    i, name, record.list_phones())
            
                i += 1
        
        return message

    def add_record(self, record):
        self.data.update({record.name.value: record})
