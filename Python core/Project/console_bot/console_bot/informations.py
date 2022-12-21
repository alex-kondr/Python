def hello(_) -> str:
    return "\nHello. How can I help you?\n\nPlease enter help for more information."


def help(_) -> str:

    info = {
        "add": "Adds name and phone number for phone book.",
        "Example_1": "add Bob +380123456789",
        "add_birhday": "Adds birthday for name in phone book",
        "Example_2": "add_birthday Bob 01.01",
        "add_note": "Adds note",
        "birthday": "Shows the number of days until the birthday",
        "Example_3": "birthday Bob",
        "contact": "show contact by type field",
        "Example_4": "contact Bob phone",
        "change": "Changes phone number to name.",
        "Example_5": "change Bob",
        "exit, close": "Exit",
        "find_contacts": "Find all contacts for mark",
        "Example_6": "find_contacts Bob, find_contacts +38012",
        "find_note": "Find all notes for mark",
        "good bye": "",
        "hello": "Prints greetings",
        "help": "Prints info",
        "remove_field": "Removes field in user",
        "Example_7": "remove_field Bob",
        "show_all": "Shows all names and phones",
        "show_notes": "Show notes"
    }

    message = "\nThis bot supports the following commands:\n\n"
    message += "|{:^13}|{:^43}|\n|".format("Command", "Information")
    message += "-" * 57 + "|\n"

    for com, inf in info.items():
        message += "|{:<13}|{:<43}|\n".format(com, inf)

    return message
