from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

from actions import Action, ADDRESS_BOOK
from fields import Field

def user_input(user_txt):
    list_command = {}

    for action in Action.list_actions:

        if action == "birthday":
            list_command.update({
                action: {
                    name: None for name in ADDRESS_BOOK.data
                }
            })
        
        elif action == "find":
            list_command.update({"find": None})

        else:
            list_command.update({
                action: {
                    field: {
                        name: None for name in ADDRESS_BOOK.data
                    } for field in Field.list_type_fields
                }
            })


    completer = NestedCompleter.from_nested_dict(list_command)

    return prompt(user_txt, completer=completer)


