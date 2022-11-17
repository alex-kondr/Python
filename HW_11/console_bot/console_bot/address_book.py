from collections import UserDict


from fields import Name, Phone, Record
from input_error import input_error


class AddressBook(UserDict):

    def __str__(self):
        message = "\n|{:^3}|{:^10}|{:^3}|{:^13}|\n".format(
            "№", "User", "№", "Phone")
        message += "-" * 35 + "\n"

        for i, (name, record) in enumerate(self.data.items()):
            message += "|{:^3}|{:^10}|{:^13}".format(
                i, name, record.list_phones())
        
        return message

    @input_error
    def add_record(self, data: str):

        name, phone = data.split()
        new_phone = Phone()
        new_phone.value = phone
        record = self.data.get(name, Record(Name(name)))
        record.add_phone(new_phone)
        self.data.update({record.name.value: record})        

        return f"The mobile phone {phone} is added to "\
            f"the user '{name}' in the phone book."

    @input_error
    def add_birthday_to_record(self, data: str):
        name, birthday = data.split()
        record = self.data.get(name)

        if not record:
            return f"User '{name}' not found on phone book."

        record.birthday.value = birthday
        return f"\nBirthday added to user '{name}'"

    @input_error
    def change_phone_in_record(self, name: str):
        record = self.data.get(name)

        if not record:
            raise ValueError(f"User '{name}' not found on phone book.")

        print("\nWhat number do you want change?")
        print(self.get_contact(name))
        number = int(
            input("Select the number in the order you want to change: "))
        mobile_phone = input("\nEnter new mobile number: ")
        record.change_phone(number, mobile_phone)

        return f"User '{name}' changed mobile phone on address book."

    @input_error
    def days_to_birthday(self, name: str) -> str:
        record = self.data.get(name, Record(Name(name)))
        return record.days_to_birthday()

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

    @input_error
    def get_contact(self, name: str):
        data = AddressBook()
        data.update({name: self.data.get(name)})

        if not self.data.get(name):
            raise ValueError(f"User '{name}' not found on phone book.")

        return data

    @input_error
    def list_contacts(self, _):        
        n = int(input("How many records to show at once. 0 - show all: "))        
        generator = self.iterator(n)
        data = None
        temp = None
        is_empty = True

        while True:
            try:                
                data = temp if temp else next(generator)
                is_empty = False
                print(data)             
                temp = next(generator)
                input("Press enter to download the next part ")               

            except StopIteration:
                message = ""
                if is_empty:
                    message = "\n|{:^3}|{:^10}|{:^3}|{:^13}|\n".format(
                        "№", "User", "№", "Phone")
                    message += "-" * 34 + "\n"
                return message

    @input_error
    def remove_phone_in_record(self, name: str) -> str:
        record = self.data.get(name)

        if not record:
            raise ValueError(f"User '{name}' not found on phone book or phone number not valid.\n")

        print("\nWhat number do you want delete?")
        print(self.get_contact(name))

        number = int(
            input("Select the number in the order you want to delete: "))
        phone = record.remove_phone(number)

        return f"\nIn user '{name}' deleted mobile phone '{phone.value}' on address book."
