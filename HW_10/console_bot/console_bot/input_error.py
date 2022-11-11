def input_error(func):
    def inner(data: str) -> str:

        message = "\n" + "-" * 55 + "\n"

        try:
            message += func(data)
            
        except ValueError:
            message += "\nEnter valid command.\nPlease enter help for more information.\n"
        
        except KeyError:
            message += "\nThis name not exists.\n"

        message += "\n" + "-" * 55 + "\n"

        return message

    return inner
