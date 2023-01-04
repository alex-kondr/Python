from termcolor import colored

def input_error(func):
    def inner(*args) -> str:

        message = "\n" + "-" * 55 + "\n"

        try:
            message += str(func(*args))

        except IndexError as error:
            message += colored(str(error), "red")

        except KeyError:
            message += colored("\nThis name not exists.\n", "red")

        except TypeError as error:
            message += colored(str(error), "red")

        except ValueError as error:
            message += colored(str(error), "red")
        
        message += "\n" + "-" * 55 + "\n"

        return message

    return inner
