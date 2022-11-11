def hello() -> str:
    return "Hello. How can I help you?\nPlease enter help for more information."


def help() -> str:

    info = {
        "add": "Adds name and phone number for phone book.",
        "Example_1": "add Bob +380123456789",
        "change": "Changes phone number to name.",
        "Example_2": "change Bob +380113456789",
        "hello": "Prints greetings",
        "help": "Prints info",
        "phone": "Shows the contact's phone number.",
        "Example_3": "phone Bob",
        "show_all": "Shows all names and phones"
    }

    message = "This bot supports the following commands:\n\n"
    message += "|{:^10}|{:^42}|\n|".format("Command", "Information")
    message += "-" * 53 + "|\n"

    for com, inf in info.items():
        message += "|{:<10}|{:<42}|\n".format(com, inf)

    return message
