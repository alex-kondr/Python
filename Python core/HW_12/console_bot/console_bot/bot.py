import actions
import informations


COMMANDS = {
    "add": actions.add,
    "add_birthday": actions.add_birthday,
    "birthday": actions.days_to_birthday,
    "change": actions.change_phone,
    "find_contacts": actions.find_contacts,
    "hello": informations.hello,
    "help": informations.help,
    "phone": actions.get_contact,
    "remove_phone": actions.remove_phone,
    "show_all": actions.show_all
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
            actions.save_data(actions.ADDRESS_BOOK, actions.FILE)
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
