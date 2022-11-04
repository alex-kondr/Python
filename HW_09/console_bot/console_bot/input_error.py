def input_error(func):
    def inner(data):

        message = "\n" + "-" * 50 + "\n"

        try:
            message += func(data)

        except TypeError:
            message += func()

        except ValueError:
            message += "\nEnter valid command.\nPlease enter help for more information.\n"

        message += "\n" + "-" * 50 + "\n"

        return message

    return inner
