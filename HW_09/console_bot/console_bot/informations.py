from input_error import input_error

@input_error
def hello():
    return "Hello. How can I help you?\nPlease enter help for more information."

@input_error
def help():

    info = {
        "add": "Adds name and phone number for phone book.|\n|"
            + " " * 10 + "Example: add Bob +380123456789",
        "change": "Changes phone number to name.|\n|"
            + " " * 10 + "Examle: change Bob +380113456789",
        "hello": "Prints greetings",
        "help": "Prints info",
        "phone": "Shows the contact's phone number.|\n|"
            + " " * 10 + "Example: phone Bob",
        "show_all": "Shows all names and phones"
    }

    message = "This bot supports the following commands:\n\n"
    message += "|{:^10}|{:^41}|\n".format("Command", "Information")
    message += "-" * 38 + "\n"

    for com, inf in info.items():
        message += "|{:<10}|{:<41}|\n".format(com, inf)

    return message
