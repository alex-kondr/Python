from actions import Action, ADDRESS_BOOK
from interface import Header, TableForContact
from fields import Record, Name


def main():

    while True:

        data = input("\nPlease enter your command: ")
        list_input_command = data.lower().split()

        while len(list_input_command) < 4:
            list_input_command += [""]

        # print(list_input_command)

        command, type_field, name, *value = list_input_command
        # print(command)
        # print(Action.list_actions)

        action = Action.list_actions.get(command)()  #type: ignore
        print(action.execute(name, type_field, value[0]))
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
