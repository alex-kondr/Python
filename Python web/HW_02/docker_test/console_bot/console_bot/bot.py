from termcolor import colored

from actions import Action
from user_input import user_input


def main():

    while True:

        data = user_input("\nPlease enter your command: ")
        list_input_command = data.strip().split()

        while len(list_input_command) < 4:
            list_input_command += [""]

        command, type_field, name, *value = list_input_command
        command = command.lower()
        type_field = type_field.lower()
        name = name.title()

        action = Action.list_actions.get(command,
            Action.list_actions.get(
                f"{command} {type_field}"))

        if action:
            action = action()
            print(action.execute(name, type_field, " ".join(value)))

        else:
            print(colored("\nEnter valid command.\n"
                  "Please enter help for more information.", "red"))
                  

if __name__ == "__main__":
    main()
