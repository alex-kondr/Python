import actions
import informations
from what_is_command import WhatIsCommand


COMMANDS = {
    "add": actions.add,
    "add_birthday": actions.add_birthday,
    "add_note": actions.add_note,
    "birthday": actions.days_to_birthday,
    "contact": actions.get_contact_for_type,
    "celebrate" : actions.contacts_celebrate_birthday,
    "change": actions.change_field,
    "find_contacts": actions.find_contacts,
    "find_note": actions.find_note,
    "hello": informations.hello,
    "help": informations.help,    
    "remove_field": actions.remove_field,
    "show_all": actions.show_all,
    "show_notes": actions.show_notes
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

        what_is_command = WhatIsCommand(list(COMMANDS))
        maybe_command = what_is_command.what_is_command(command)

        if check_exit(data):
            print(check_exit(data))
            actions.save_data(actions.ADDRESS_BOOK, actions.ADDRESS_BOOK_FILE)
            actions.save_data(actions.NOTE, actions.NOTE_FILE)
            quit()

        elif command in COMMANDS:
            data = data[len(command)+1:]
            command = COMMANDS[command]
            message = command(data)

        elif input(f"If you mean '{maybe_command}' enter 'y': ") == "y":
            data = data[len(command)+1:]
            command = COMMANDS[maybe_command]
            message = command(data)


        # 

        # else:
        #     message = "\n" + "-" * 50 + "\n"
        #     message += "Enter valid command.\n"\
        #         "Please enter help for more information."
        #     message += "\n" + "-" * 50 + "\n"
        else:
            message = ""

        print(message)


if __name__ == "__main__":
    main()
