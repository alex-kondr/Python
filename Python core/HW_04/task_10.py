from random import randint


def get_random_password():

    password = ""

    for _ in range(8):
        password += chr(randint(40, 126))

    return password
