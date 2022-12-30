from abc import ABC, abstractmethod
from datetime import datetime
import re


class Field(ABC):

    def __init__(self, value):
        self._value = None
        self.value = value

    def type_of_field(self):
        return type(self).__name__

    @property
    def value(self):
        return self._value

    
    @value.setter
    @abstractmethod
    def value(self, value):
        pass


class Address(Field):

    @Field.value.setter
    def value(self, value: str):
        self._value = value


class Birthday(Field):

    @Field.value.setter
    def value(self, data: str):

        birthday = re.search(r"\d{2}\.\d{2}", data)

        if not birthday:
            raise ValueError("Birthday not valid.\n"
                "The Birthday should look like '01.01'")

        self._value = datetime.strptime(birthday.group(), "%d.%m")


class Email(Field):

    @Field.value.setter
    def value(self, value: str):
        self._value = value


class Name(Field):
    
    @Field.value.setter
    def value(self, value: str):
        self._value = value


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

        # self.birthday = None
        # self.name = name
        self.fields = {name.type_of_field(): [name]}

    def add_field(self, field: Field):

        if not self.fields.get(field.type_of_field()):
            self.fields.update({field.type_of_field(): [field]})
        
        else:
            self.fields[field.type_of_field()].append(field)

    def change_field(self, type_field: str, number_in_list: int, new_field: str):
        self.fields[type_field][number_in_list].value = new_field

    # def days_to_birthday(self):

    #     if not self.birthday:
    #         raise ValueError("Birthday not specified")

    #     now_date = datetime.now()
    #     birthday = self.birthday.value.replace(year=now_date.year)

    #     return (birthday - now_date).days + 1    

    def types_of_fields(self) -> list:

        fields = []

        for type_of_field in self.fields:
            fields += ["№", type_of_field]
        
        return fields

    def remove_field(self, number_in_list: int, type_field: str):
        return self.fields[type_field].pop(number_in_list)
