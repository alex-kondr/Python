import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite


class Contacts:
    count_save = 0

    def __init__(self, filename: str, contacts: list[Person] = None):  # type: ignore
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts
        # self.count_save = 0

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)
        self.count_save -= 1
    
    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
            # self.count_save += 1
        return content

    
    def __getstate__(self):
        # pass

        attributes = self.__dict__.copy()
        # attributes['file'] = None
        self.count_save += 1
        # # Contacts.count()
        return attributes

    # @classmethod
    # def count(cls):
    #     # cls.count_save += 1
    #     return cls.count_save
        


contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
first = persons.read_from_file()
first.save_to_file()
second = first.read_from_file()
second.save_to_file()
third = second.read_from_file()

print("person: ", persons.count_save)  # 0
print("first: ", first.count_save)  # 1
print("second: ", second.count_save)  # 2
print("third: ", third.count_save)  # 3
