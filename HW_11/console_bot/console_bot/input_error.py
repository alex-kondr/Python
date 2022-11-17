def input_error(func):
    def inner(self, data: str) -> str:

        message = "\n" + "-" * 55 + "\n"

        try:
            message += str(func(self, data))

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
