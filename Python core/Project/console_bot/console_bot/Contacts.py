from datetime import datetime
import re


class Field:

    def __init__(self, value):
        self._value = None
        self.value = value

    def type(self):
        return type(self).__name__

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Address(Field):
    pass


class Birthday(Field):

    @Field.value.setter
    def value(self, data: str):

        birthday = re.search(r"\d{2}\.\d{2}", data)

        if not birthday:
            raise ValueError("Birthday not valid.\n"
                "The Birthday should look like '01.01'")

        self._value = datetime.strptime(birthday.group(), "%d.%m")


class Email(Field):
    pass


class Name(Field):
    pass


class Phone(Field):

    @Field.value.setter
    def value(self, phone: str):
        new_phone = re.search(r"\+380\d{9}", phone)

        if not new_phone:
            raise ValueError("Phone number not valid.\n"\
                "The phone number should look like +380123456789")
        
        self._value = new_phone.group()


class Record:

    def __init__(self, name: Name):

        self.birthday = None
        self.name = name
        self.fields = {}

    def add_field(self, field: Field):

        if not self.fields.get(field.type()):
            self.fields.update({field.type(): [field]})
        
        else:
            self.fields[field.type()].append(field)

    def change_field(self, type_field: str, number_in_list: int, new_field: str):
        self.fields[type_field][number_in_list].value = new_field

    def days_to_birthday(self):

        if not self.birthday:
            raise ValueError("Birthday not specified")

        now_date = datetime.now()
        birthday = self.birthday.value.replace(year=now_date.year)

        return (birthday - now_date).days + 1

    def list_fields(self) -> str:
        fields = ""

        for i, (type, list_field) in enumerate(self.fields.items()):
            temp = ""

            if i > 0:
                fields += "|{:^3}|{:^10}|".format(" ", " ")
            
            for j, field in enumerate(list_field):
                if j > 0:
                    temp += "|{:^3}|{:^10}|{:^3}|{:^10}|".format(" ", " ", " ", " ", " ")

                temp += "{:^3}|{:^13}|\n".format(j, field.value)

            fields += "{:^3}|{:^10}|{:^13}".format(i, type, temp)

        return fields

    def remove_field(self, number_in_list: int):
        return self.fields.pop(number_in_list)


# if __name__ == "__main__":

#     phone = Phone("+380509228157")
#     record = Record("111")
#     record.add_contact(phone)

#     phone = Phone("+380509228158")
#     record.add_contact(phone)

#     email = Email("456")
#     record.add_contact(email)
#     print(phone)
#     print(record.list_fields())
