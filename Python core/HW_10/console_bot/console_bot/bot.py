import actions
import informations


ACTIONS = {
    "add": actions.add,
    "change": actions.change,    
    "phone": actions.phone,
    "remove_phone": actions.remove_phone    
}

INFORMATIONS = {
    "hello": informations.hello,
    "help": informations.help,
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
