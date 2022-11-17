from address_book import AddressBook
import informations


ADDRESS_BOOK = AddressBook()


COMMANDS = {
    "add": ADDRESS_BOOK.add_record,
    "add_birthday": ADDRESS_BOOK.add_birthday_to_record,
    "birthday": ADDRESS_BOOK.days_to_birthday,
    "change": ADDRESS_BOOK.change_phone_in_record,
    "hello": informations.hello,
    "help": informations.help,
    "phone": ADDRESS_BOOK.get_contact,
    "remove_phone": ADDRESS_BOOK.remove_phone_in_record,
    "show_all": ADDRESS_BOOK.list_contacts
}


def check_exit(data: str):

    exit = ("good bye", "exit", "close")

    for text in exit:
        if text in data.lower():
            return "\nGood bye\n"

def main():
    
    while True:

        data = input("\nPlease enter your command: ")
        command = data.lower().split()[0] if data else ""

        if check_exit(data):
            print(check_exit(data))
            quit()

        elif command in COMMANDS:
            data = data[len(command)+1:]
            command = COMMANDS[command]
            message = command(data)

        else:
            message = "\n" + "-" * 50 + "\n"
            message += "Enter valid command.\n"\
                "Please enter help for more information."
            message += "\n" + "-" * 50 + "\n"

        print(message)


if __name__ == "__main__":
    main()
