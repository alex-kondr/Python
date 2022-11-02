"""USERS = {"name": "phone"}"""


USERS = {}

"""COMMANDS = {"command": func}"""
# COMMANDS = {"add": add()}


def add(name, phone): 
    USERS.update({name: phone})

def input_error():
    pass
    

def change(name, phone):
    USERS.update({name: phone})

def hello():
    pass

def phone():
    pass

def show_all():
    pass

COMMANDS = {
    "add": add,
    "change": change,
    "hello": hello,
    "phone": phone,
    "show_all": show_all
}


def main():

    # COMMANDS = {
    #     "add": add(new_command[1], new_command[2]),
    #     }

    while True:

        in_command = input("Please enter 'add name phone': ").split()
        in_command = dict(enumerate(in_command))

        command = COMMANDS.get(in_command.get(0))
        command(in_command.get(1), in_command.get(2))


        # if in_command[0] == "add":
            
        #     name = in_command[1]

        #     if USERS.get(name):
        #         print(f"User {name} already exists")
        #         print("If you want change this name please input 'change name phone'")
        #         continue

        #     phone = in_command[2]
        #     add_change(name, phone)

        # elif in_command[0] == "change":
        #     name = in_command[1]
        #     phone = in_command[2]
        #     add_change(name, phone)

        # elif in_command[0] =="phone":
        #     name = in_command[1]

        #     if not USERS.get(name):
        #         print(f"User {name} is not exists")
        #         continue

        #     print(f"{name}: {USERS.get(name)}")
                
            

        # COMMANDS[new_command[0]]

        # add(new_user)
        print(USERS)

if __name__ == "__main__":    
    main()
