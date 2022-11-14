def input_error(func):
    def inner(data: str) -> str:

        message = "\n" + "-" * 55 + "\n"

        try:
            message += func(data)

        except IndexError as error:
            message += str(error)    

        except KeyError:
            message += "\nThis name not exists.\n" 

        except ValueError:
            message += "\nEnter valid command.\nPlease enter help for more information.\n"
        
        message += "\n" + "-" * 55 + "\n"

        return message

    return inner
