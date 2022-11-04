USERS = {}
EXIT = ("good bye", "exit", "close")


def input_error(func):
    def inner(data):

        try:
            message = func(data)
        except TypeError:
            func()
            # print("ups")
        return message

    return inner

@input_error
def add(data):

    name, phone = data.split()
    USERS.update({name: phone})

    return f"User {name} added to phone book"


@input_error
def change(data):

    name, phone = data.split()
    
    if name in USERS:        
        USERS.update({name: phone})
        return f"User {name} changed on phone book"

    return f"User {name} not found on phone book"

@input_error
def hello(_):

    info = {
        "add": "add (name) (phone)",
        "change": "change (name) (phone)",
        "hello": "print info",
        "phone": "phone (name)",
        "show_all": "show all names and phones"}

    message = "How can I help you?\n"
    message += "This bot supports the following commands:\n\n"
    message += "|{:^8}|{:^25}|\n".format("Command", "Information")
    message += "-" * 38 + "\n"

    for com, inf in info.items():
        message += "|{:<10}|{:<25}|\n".format(com, inf)
    
    return message

@input_error
def phone(data):

    name = data
    message = "|{:^10}|{:^10}|\n".format("User", "Phone")
    message += "-" * 23 + "\n"
    message += "|{:^10}|{:<10}|\n".format(name, USERS[name])

    return message

@input_error
def show_all(_):

    message = "|{:^10}|{:^10}|\n".format("User", "Phone")
    message += "-" * 23 + "\n"

    for name, phone in USERS.items():        
        message += "|{:^10}|{:<10}|\n".format(name, phone)

    return message

COMMANDS = {
    "add": add,
    "change": change,
    "hello": hello,
    "phone": phone,
    "show_all": show_all
}

def main():

    while True:

        data = input("Please enter your command: ")
        command = data.lower().split()[0]

        if command in EXIT:
            print("Good bye!")
            quit()

        if command in COMMANDS:
            data = data[len(command)+1:]
            command = COMMANDS[command]
            message = command(data)

        print(message) 

if __name__ == "__main__":
    main()

