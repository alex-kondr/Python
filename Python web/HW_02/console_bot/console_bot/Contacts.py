from abc import ABCMeta, abstractmethod
from datetime import datetime
import re


class Field(metaclass=ABCMeta):

    def __init__(self, value):
        self._value = None
        self.value = value
   
    @abstractmethod
    def list_values(self):
        pass

    def type(self):
        return type(self).__name__

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Birthday(Field):

    @Field.value.setter
    def value(self, data: str):

        birthday = re.search(r"\d{2}\.\d{2}", data)

        if not birthday:
            raise ValueError("Birthday not valid.\n"
                             "The Birthday should look like '01.01'")

        self._value = datetime.strptime(birthday.group(), "%d.%m")

    def list_values(self):
        pass


class Address(Field):

    def list_values(self):
        pass


class Email(Field):

    def list_values(self):
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

    def list_values(self):
        pass
        # fields = ""

        # for i, field in enumerate(self.fields):
        #     if i > 0:
        #         fields += "|{:^3}|{:^10}|".format(" ", " ")

        #     fields += "{:^3}|{:^13}|\n".format(i, field.value)

        # return fields


class Record:

    def __init__(self, name):

        self.birthday = None
        self.name = name
        self.fields = {}

    def add_contact(self, field: Field):

        if not self.fields.get(field.type()):
            self.fields.update({field.type(): [field]})
        
        else:
            self.fields[field.type()].append(field)

    def list_fields(self) -> str:
        fields = ""

        for i, (type, list_field) in enumerate(self.fields.items()):
            temp = ""
            
            for field in list_field:
                temp += field.value + "|"
                
            # if i > 0:
            #     fields += "|{:^3}|{:^10}|{:^10}|".format(" ", " ", " ")

            fields += "{:^3}|{:^10}|{:^13}|\n".format(i, type, temp[:-1])

        return fields


phone = Phone("+380509228157")
record = Record("111")
record.add_contact(phone)

phone = Phone("+380509228158")
record.add_contact(phone)

email = Email("456")
record.add_contact(email)

print(record.list_fields())
