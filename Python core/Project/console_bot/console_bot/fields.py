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

    @Field.value.setter
    def value(self, email: str):
        new_email = re.search(r".+@.+", email)

        if not new_email:
            raise ValueError("Email not valid.")

        self._value = new_email.group()


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

        if self.fields.get(field.type()):
            self.fields[field.type()].append(field)
        
        else:
            self.fields.update({field.type(): [field]})
            

    def change_field(self, type_field: str, number_in_list: int, new_field: str):
        self.fields[type_field][number_in_list].value = new_field

    def days_to_birthday(self):

        if not self.birthday:
            raise ValueError("Birthday not specified")

        now_date = datetime.now()
        birthday = self.birthday.value.replace(year=now_date.year)

        return (birthday - now_date).days + 1    

    def remove_field(self, number_in_list: int, type_field: str):
        return self.fields[type_field].pop(number_in_list)
