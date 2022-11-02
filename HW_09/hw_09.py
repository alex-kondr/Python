"""USERS = {"name": "phone"}"""


USERS = {}
EXIT = ("good bye", "exit", "close")


def input_error(func):
    def inner(data):

        try:
            func(data)
        except TypeError:
            func()
            # print("ups")

    return inner

@input_error
def add(data):
    USERS.update({data.get(1): data.get(2)})
   
@input_error
def change(data):
    USERS.update({data.get(1): data.get(2)})

@input_error
def hello():

    info = {
        "add": "add (name) (phone)",
        "change": "change (name) (phone)",
        "hello": "print info",
        "phone": "phone (name)",
        "show_all": "show all names and phones"}
    print("How can I help you?")
    print("This bot supports the following commands:")

    for com, inf in info.items():
        print(f"{com}: {inf}")

def phone(data):
    return USERS.get(data.get(1))

def show_all(_):
    for name, phone in USERS.items():
        pass
    
    return f""

COMMANDS = {
    "add": add,
    "change": change,
    "hello": hello,
    "phone": phone,
    "show_all": show_all
}


def main():
    

    while True:
        

        data = input("Please enter 'add name phone': ").split()
        data = dict(enumerate(data))

        if data.get(0).lower() in EXIT:
            print("Good bye!")
            quit()

        command = COMMANDS.get(data.get(0).lower())
        print(command(data) or "Please input new command")

        # print(USERS)

if __name__ == "__main__":    
    main()
