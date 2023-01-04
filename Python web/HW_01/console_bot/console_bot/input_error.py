def input_error(func):
    def inner(*args) -> str:

        message = "\n" + "-" * 55 + "\n"

        try:
            message += str(func(*args))

        except IndexError as error:
            message += str(error)    

        except KeyError:
            message += "\nThis name not exists.\n"

        except TypeError as error:
            message += str(error)

        except ValueError as error:
            message += str(error)
        
        message += "\n" + "-" * 55 + "\n"

        return message

    return inner
