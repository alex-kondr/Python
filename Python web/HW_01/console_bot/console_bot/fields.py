from abc import ABC, abstractmethod
from collections import UserDict, UserList
from datetime import datetime
import re


class Field(ABC):

    list_type_fields = {}

    def __init_subclass__(cls) -> None:
        Field.list_type_fields.update(
            {cls.__name__.lower(): cls}
        )

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

    def __init__(self, value):
        super().__init__(value)
        self.birthday = None

    @Field.value.setter
    def value(self, data: str):

        birthday = re.search(r"\d{2}\.\d{2}.\d{4}", data)

        if not birthday:
            raise ValueError("Birthday not valid.\n"
                "The Birthday should look like '01.01.1900'")

        self._value = birthday.group()
        self.birthday = datetime.strptime(birthday.group(), "%d.%m.%Y")
        


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

    def list_values(self) -> list[str]:
        return [field.value for field in self.data]

    def max_len_value(self) -> int:
        len_values = [len(field.value) for field in self.data]

        return max(len_values)


class Record(UserDict):

    def __init__(self, name: Name):
        super().__init__()

        self.name = name
        
        # list_fields = ListFields(name.type_of_field())
        # list_fields.add_field(name)
        # self.data.update({name.type_of_field(): list_fields})

    def add_field(self, field: Field) -> None:

        list_fields = self.data.get(field.type_of_field(), ListFields(field.type_of_field()))
        list_fields.add_field(field)
        self.data.update({field.type_of_field(): list_fields})

    def change_field(self, type_field: str, number_in_list: int, new_field: str) -> None:
        self.data[type_field][number_in_list].value = new_field

    def days_to_birthday(self):

        birthday = self.data.get("Birthday")

        if not birthday:
            raise ValueError("Birthday not specified")

        now_date = datetime.now()
        birthday = birthday[0].birthday.replace(year=now_date.year)

        return (birthday - now_date).days + 1

    def list_len_cells(self) -> list[int]:
        return [list_fields.max_len_value() for list_fields in self.values()]

    def types_of_fields(self) -> list[str]:
        fields = [type_of_field for type_of_field in self.data]
        return fields

    def remove_field(self, number_in_list: int, type_field: str):
        return self.data[type_field].pop(number_in_list)


# name = Name("alex")
# # print(Field.list_fields)
# # print(Field.list_fields)
# # name = Name("alex")
# # print(name.value)
# phone = Phone("+380509228157")
# # list_filds = ListFields(phone.type_of_field())
# # # list_filds.add_field(phone)
# # # print(list_filds.type_of_field)
# record = Record(name)
# # print(record.data)
# phone1 = Phone("+380509228156")
# record.add_field(phone)
# record.add_field(phone1)
# print(record.get_contact())
# email = Email("alex_kondr@outlook.com")
# record.add_field(email)
# print(record.max_len_value())
# record.add_field(phone1)
# print(record.data)

# list_fields = record.data.get(phone.type_of_field())
# for field in list_fields.data:
#     print(field.value)
