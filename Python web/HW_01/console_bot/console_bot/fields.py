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

    @Field.value.setter
    def value(self, value: str):

        birthday = re.search(r"\d{2}\.\d{2}.\d{4}", value)

        if not birthday:
            raise ValueError("Birthday not valid.\n"
                "The Birthday should look like '01.01.1900'")

        self._value = birthday.group()


class Email(Field):

    @Field.value.setter
    def value(self, value: str):

        email = re.search(r"\.+@\.+", value)

        if not email:
            raise ValueError("Email not valid.\n"
                    "The Email should look like 'mike@host.com'")

        self._value = email.group()


class Name:

    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value: str):
        self._value = value


class Note(Field):

    @Field.value.setter
    def value(self, value: str):
        self._value = value


class Phone(Field):

    @Field.value.setter
    def value(self, value: str):
        new_phone = re.search(r"\+380\d{9}", value)

        if not new_phone:
            raise ValueError("Phone number not valid.\n"\
                "The phone number should look like +380123456789")
        
        self._value = new_phone.group()


class Tag(Field):

    @Field.value.setter
    def value(self, value: str):


        tag = re.search(r"#.+", value)
        print(tag, value)

        if not tag:
            raise ValueError("Tag not valid.\n"\
                "The tag must be start '#'")

        self._value = tag.group()


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

    def add_field(self, field: Field) -> None|str:

        if (field.type_of_field() == "Birthday" and 
                self.data.get("Birthday")):

            raise ValueError("A birthday has already been added to this contact")          

        list_fields = self.data.get(field.type_of_field(), ListFields(field.type_of_field()))
        list_fields.add_field(field)
        self.data.update({field.type_of_field(): list_fields})

    def change_field(self, type_field: str, number_in_list: int, new_field: str) -> None:
        self.data[type_field][number_in_list].value = new_field

    def days_to_birthday(self):

        birthday = self.get_values("Birthday")

        # if not birthday:
        #     raise ValueError("Birthday not specified")

        now_date = datetime.now()
        birthday = datetime.strptime(birthday[0], "%d.%m.%Y")

        birthday = birthday.replace(
            year=now_date.year) if birthday.month > now_date.month else birthday.replace(year=now_date.year+1)

        return (birthday - now_date).days + 1

    def get_values(self, type_field: str) -> list[str]:
        list_fields = self.data.get(type_field)

        if not list_fields:
            raise ValueError(f"This contact not specified field '{type_field}'")
        
        return list_fields.list_values()

    def list_len_cells(self) -> list[int]:
        return [list_fields.max_len_value() for list_fields in self.values()]

    def types_of_fields(self) -> list[str]:
        fields = [type_of_field for type_of_field in self.data]
        return fields

    def remove_field(self, number_in_list: int, type_field: str) -> str:
        return self.data[type_field].pop(number_in_list)
