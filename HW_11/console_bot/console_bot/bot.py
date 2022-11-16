import actions
# from address_book import AddressBook, Name, Phone, Record
import informations


# ADDRESS_BOOK = actions.ADDRESS_BOOK


ACTIONS = {
    "add": actions.ADDRESS_BOOK.add_record,
    "change": actions.change,    
    "phone": actions.ADDRESS_BOOK.get_contact,
    "remove_phone": actions.remove_phone    
}

INFORMATIONS = {
    "hello": informations.hello,
    "help": informations.help,
    "show_all": actions.ADDRESS_BOOK.list_contacts
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

        elif command in ACTIONS:
            data = data[len(command)+1:]
            command = ACTIONS[command]
            message = command(data)

        elif command in INFORMATIONS:
            command = INFORMATIONS[command]
            message = command()

        else:
            message = "\n" + "-" * 50 + "\n"
            message += "Enter valid command.\n"\
                "Please enter help for more information."
            message += "\n" + "-" * 50 + "\n"

        print(message)


if __name__ == "__main__":
    main()
