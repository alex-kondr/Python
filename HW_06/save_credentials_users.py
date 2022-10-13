from pathlib import Path


path = Path("HW_06/output.txt")
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}

def save_credentials_users(path, users_info):

    with open(path, "wb") as file:

        for user, password in users_info.items():
            file.write(f"{user}:{password}\n".encode())



save_credentials_users(path, users_info)

        

