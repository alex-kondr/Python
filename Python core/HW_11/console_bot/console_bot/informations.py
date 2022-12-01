def hello(_) -> str:
    return "\nHello. How can I help you?\n\nPlease enter help for more information."


def help(_) -> str:

    info = {
        "add": "Adds name and phone number for phone book.",
        "Example_1": "add Bob +380123456789",
        "add_birhday": "Adds birthday for name in phone book",
        "Example_2": "add_birthday Bob 01.01",
        "birthday": "Shows the number of days until the birthday",
        "Example_3": "birthday Bob",
        "change": "Changes phone number to name.",
        "Example_4": "change Bob",
        "exit, close": "Exit",
        "good bye": "",
        "hello": "Prints greetings",
        "help": "Prints info",
        "phone": "Shows the contact's phone number.",
        "Example_5": "phone Bob",
        "remove_phone": "Removes mobile phone in user",
        "Example_6": "remove_phone Bob",
        "show_all": "Shows all names and phones"
    }

    message = "\nThis bot supports the following commands:\n\n"
    message += "|{:^13}|{:^43}|\n|".format("Command", "Information")
    message += "-" * 57 + "|\n"

    for com, inf in info.items():
        message += "|{:<13}|{:<43}|\n".format(com, inf)

    return message
