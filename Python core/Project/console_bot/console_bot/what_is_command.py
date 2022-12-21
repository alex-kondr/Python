commands = ['add', 'add_birthday', 'add_note', 'birthday', 'contact', 'celebrate', 'change',
    'find_contacts', 'find_note', 'hello', 'help', 'remove_field', 'show_all', 'show_notes']


class WhatIsCommand:

    def __init__(self, commands: list):
        self.commands = commands

    def what_is_command(self, command_in: str) -> str:
        count = 0
        command_out = ""

        for command in self.commands:

            i = 0

            for char_in, char_comm in zip(command_in, command):

                if char_in == char_comm:
                    i += 1

            if i > count:
                count = i
                command_out = command

        return command_out


# a = WhatIsCommand(commands)

# print(a.what_is_command("exit"))
