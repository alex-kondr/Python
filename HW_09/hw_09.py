USERS = {}
EXIT = ("good bye", "exit", "close")


def input_error(func):
    def inner(data):

        message = "\n" + "-" * 50 + "\n"

        try:
            message += func(data)

        except TypeError:
            message += func()
            
        except ValueError:
            message += info()

        message += "\n" + "-" * 50 + "\n"

        return message

    return inner


@input_error
def add(data):

    name, phone = data.split()

    if name not in USERS:
        USERS.update({name: phone})
        return f"User '{name}' added to phone book"
    
    return "User '{name}' already exist"


def check_exit(data):

    for text in EXIT:
        if text in data:
            return "\nGood bye\n"


@input_error
def change(data):

    name, phone = data.split()

    if name in USERS:
        USERS.update({name: phone})
        return f"User '{name}' changed on phone book"

    return f"User '{name}' not found on phone book"


@input_error
def hello():

    return "Hello. How can I help you?\nPlease enter help for more information."


@input_error
def help():

    info = {
        "add": "add (name) (phone)",
        "change": "change (name) (phone)",
        "hello": "prints greetings",
        "help": "prints info",
        "phone": "phone (name)",
        "show_all": "show all names and phones"}

    message = "This bot supports the following commands:\n\n"
    message += "|{:^10}|{:^25}|\n".format("Command", "Information")
    message += "-" * 38 + "\n"

    for com, inf in info.items():
        message += "|{:<10}|{:<25}|\n".format(com, inf)

    return message

# @input_error
def info():
    return "Enter valid command.\nPlease enter help for more information."


@input_error
def phone(data):

    name = data
    message = "|{:^10}|{:^10}|\n".format("User", "Phone")
    message += "-" * 23 + "\n"
    message += "|{:^10}|{:<10}|".format(name, USERS[name])

    return message


@input_error
def show_all():

    message = "|{:^10}|{:^10}|\n".format("User", "Phone")
    message += "-" * 23 + "\n"

    for name, phone in USERS.items():
        message += "|{:^10}|{:<10}|".format(name, phone)

    return message


COMMANDS = {
    "add": add,
    "change": change,
    "hello": hello,
    "help": help,
    "phone": phone,
    "show_all": show_all
}


def main():

    while True:

        data = input("Please enter your command: ")
        command = data.lower().split()[0] if data else ""

        if check_exit(data):
            print(check_exit(data))
            quit()

        elif command in COMMANDS:

            data = data[len(command)+1:]
            command = COMMANDS[command]
            message = command(data)

        else:
            message = info()

        print(message)


if __name__ == "__main__":
    main()
