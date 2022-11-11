from collections import UserDict


class Field:
    pass


class Name(Field):

    def __init__(self, name: str):
        self.value = name


class Phone(Field):

    def __init__(self):    
        self.mobile_phone = ""
        self.home_phone = ""
        self.email = ""


class Record(Field):

    def __init__(self, name: Name):
        self.name = name
        self.phones = []

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_phone(self, old_number: str, new_number: str):
        phone = list(
            filter(lambda phone: phone.mobile_phone == old_number, self.phones))

        if len(phone) > 0:
            phone[0].mobile_phone = new_number

    def remove_phone(self, phone_value: str):

        phone = list(
            filter(lambda phone: phone.mobile_phone == phone_value, self.phones))

        if len(phone) > 0:
            self.phones.remove(phone[0])


class AddressBook(UserDict):

    # count = 0

    def add_record(self, record: Record):
        self.data.update({record.name.value: record})
        # AddressBook.count += 1

    def get_contact(self, name: str):
        return self.data.get(name)

    def list_contacts(self) -> dict:
        return self.data
