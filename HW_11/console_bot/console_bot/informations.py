def hello() -> str:
    return "\nHello. How can I help you?\n\nPlease enter help for more information."


def help() -> str:

    info = {
        "add": "Adds name and phone number for phone book.",
        "Example_1": "add Bob +380123456789",
        "change": "Changes phone number to name.",
        "Example_2": "change Bob",
        "exit, close": "Exit",
        "good bye": "",
        "hello": "Prints greetings",
        "help": "Prints info",
        "phone": "Shows the contact's phone number.",
        "Example_3": "phone Bob",
        "remove_phone": "Removes mobile phone in user",
        "Example_3": "remove_phone Bob",
        "show_all": "Shows all names and phones"
    }

    message = "\nThis bot supports the following commands:\n\n"
    message += "|{:^13}|{:^42}|\n|".format("Command", "Information")
    message += "-" * 56 + "|\n"

    for com, inf in info.items():
        message += "|{:<13}|{:<42}|\n".format(com, inf)

    return message
