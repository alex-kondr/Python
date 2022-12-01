from address_book import AddressBook
from fields import Birthday, Name, Phone, Record
from input_error import input_error


ADDRESS_BOOK = AddressBook()


@input_error
def add(data: str) -> str:
    name, phone = data.split()
    new_phone = Phone(phone)
    record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
    record.add_phone(new_phone)
    ADDRESS_BOOK.add_record(record)

    return f"The mobile phone {phone} is added to "\
        f"the user '{name}' in the phone book."


@input_error
def add_birthday(data: str):
    name, birthday = data.split()
    record = ADDRESS_BOOK.data.get(name)

    if not record:
        return f"User '{name}' not found on phone book."

    record.birthday = Birthday(birthday)
    return f"\nBirthday added to user '{name}'"


@input_error
def change_phone(name: str):
    record = ADDRESS_BOOK.data.get(name)

    if not record:
        raise ValueError(f"User '{name}' not found on phone book.")

    print("\nWhat number do you want change?")
    print(get_contact(name))
    number = int(
        input("Select the number in the order you want to change: "))
    mobile_phone = input("\nEnter new mobile number: ")
    record.change_phone(number, mobile_phone)

    return f"User '{name}' changed mobile phone on address book."


@input_error
def days_to_birthday(name: str) -> str:
    record = ADDRESS_BOOK.data.get(name, Record(Name(name)))
    return record.days_to_birthday()


@input_error
def get_contact(name: str):
    data = AddressBook()
    data.update({name: ADDRESS_BOOK.data.get(name)})

    if not ADDRESS_BOOK.data.get(name):
        raise ValueError(f"User '{name}' not found on phone book.")

    return data


@input_error
def remove_phone(name: str) -> str:
    record = ADDRESS_BOOK.data.get(name)

    if not record:
        raise ValueError(
            f"User '{name}' not found on phone book or phone number not valid.\n")

    print("\nWhat number do you want delete?")
    print(get_contact(name))

    number = int(
        input("Select the number in the order you want to delete: "))
    phone = record.remove_phone(number)

    return f"\nIn user '{name}' deleted mobile phone '{phone.value}' on address book."


def show_all(_):
    temp = None
    is_empty = True

    try:
        n = int(input("How many records to show at once. 0 - show all: "))
        generator = ADDRESS_BOOK.iterator(n)

        while True:
            temp = temp if temp else next(generator)
            is_empty = False
            print(temp)
            temp = next(generator)
            input("Press enter to download the next part ")

    except StopIteration:
        message = ""
        if is_empty:
            message = "\n|{:^3}|{:^10}|{:^3}|{:^13}|\n".format(
                "№", "User", "№", "Phone")
            message += "|" + "-" * 32 + "|\n"
        return message

    except ValueError:
        return "\nThis is not number"
