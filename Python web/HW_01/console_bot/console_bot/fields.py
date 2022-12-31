from abc import ABC, abstractmethod
from collections import UserDict, UserList
from datetime import datetime
import re


class Field(ABC):

    list_fields = {}

    def __init_subclass__(cls) -> None:
        Field.list_fields.update({cls.__name__: cls})

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


class ListFields(UserList):

    def __init__(self, type_of_field) -> None:
        super().__init__()
        self.type_of_field = type_of_field

    def add_field(self, field):        
        self.data.append(field)

    def list_values(self) -> list:
        # values = [field.value for field in self.data]
        return [field.value for i, field in enumerate(self.data)]

        # for field in self.data:



class Record(UserDict):

    def __init__(self, name: Name):
        super().__init__()

        # self.birthday = None
        # self.name = name
        list_fields = ListFields(name.type_of_field())
        list_fields.add_field(name)
        self.data.update({name.type_of_field(): list_fields})

    def add_field(self, field: Field):

        # list_fields = ListFields()
        # list_fields.add_field(field)

        list_fields = self.data.get(field.type_of_field(), ListFields(field.type_of_field()))
        list_fields.add_field(field)
        self.data.update({field.type_of_field(): list_fields})

        # if not self.fields.get(field.type_of_field()):
        #     self.fields.update({field.type_of_field(): [field]})
        
        # else:
        #     self.fields[field.type_of_field()].append(field)

    def change_field(self, type_field: str, number_in_list: int, new_field: str):
        self.data[type_field][number_in_list].value = new_field

    # def days_to_birthday(self):

    #     if not self.birthday:
    #         raise ValueError("Birthday not specified")

    #     now_date = datetime.now()
    #     birthday = self.birthday.value.replace(year=now_date.year)

    #     return (birthday - now_date).days + 1    

    def types_of_fields(self) -> list:

        fields = []

        for type_of_field in self.data:
            fields += ["№", type_of_field]
        
        return fields

    def remove_field(self, number_in_list: int, type_field: str):
        return self.data[type_field].pop(number_in_list)


# name = Name("alex")
# print(Field.list_fields)
# print(Field.list_fields)
# name = Name("alex")
# print(name.value)
# phone = Phone("+380509228157")
# # list_filds = ListFields(phone.type_of_field())
# # list_filds.add_field(phone)
# # print(list_filds.type_of_field)
# record = Record(name)
# print(record.data)
# phone1 = Phone("+380509228156")
# record.add_field(phone)
# print(record.data)
# record.add_field(phone1)
# print(record.data)

# list_fields = record.data.get(phone.type_of_field())
# for field in list_fields.data:
#     print(field.value)
