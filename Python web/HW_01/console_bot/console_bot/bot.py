from actions import Action
from user_input import user_input


def main():

    while True:

        data = user_input("\nPlease enter your command: ")
        list_input_command = data.strip().split()

        while len(list_input_command) < 4:
            list_input_command += [""]

        # print(list_input_command)

        command, type_field, name, *value = list_input_command
        command = command.lower()
        type_field = type_field.lower()
        name = name.title()

        # print(command)
        # print(Action.list_actions)

        action = Action.list_actions.get(command,
            Action.list_actions.get(
                f"{command} {type_field}"))

        if action:
            action = action()
            # print(action)

        else:
            print("Enter valid command.\n"
                  "Please enter help for more information.")
            continue

        # print("name_bot: ", name)
        
        print(action.execute(name, type_field, " ".join(value)))
        # record = ADDRESS_BOOK.data.get(name, Record(Name(name)))

        
        # header = Header(record)
        # one_line = TableForContact(record)
        # line = header.create_line()
        # line += one_line.create_line()
        # print(line)




if __name__ == "__main__":
    main()

# command = "add".lower()
# type_field = "phone".lower()
# name = "alex"
# value = "+380509228157"

# action = Action.list_actions.get(command)()
# # print(action)
# print(action.execute(name, type_field, value))
# print(ADDRESS_BOOK.data)
