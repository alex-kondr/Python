import shutil
from pathlib import Path

path = Path("HW_06/")
file_name = Path("output.txt")
employee_residence = {'Michael': 'Canada', 
                      'John': 'USA', 
                      'Liza': 'Australia'}

def create_backup(path, file_name, employee_residence):
    
    with open(f"{path}/{file_name}", "wb") as file:

        for key, value in employee_residence.items():
            file.write(f"{key} {value}\n".encode())

    return shutil.make_archive("backup_folder", "zip", path)




create_backup(path, file_name, employee_residence)
