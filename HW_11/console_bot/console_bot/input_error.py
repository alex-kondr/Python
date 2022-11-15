def input_error(func):
    def inner(data: str) -> str:

        message = "\n" + "-" * 55 + "\n"

        try:
            message += func(data)

        except IndexError as error:
            message += str(error)    

        except KeyError:
            message += "\nThis name not exists.\n" 

        except ValueError as error:
            message += str(error)
        
        message += "\n" + "-" * 55 + "\n"

        return message

    return inner
