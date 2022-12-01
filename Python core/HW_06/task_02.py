from pathlib import Path

employee_list = [['Robert Stivenson,28',
                  'Alex Denver,30'],
                  ['Drake Mikelsson,19']]

path = Path('G:/Мій диск/Мої проекти/Python/txt.txt')

def write_employees_to_file(employee_list, path):
    fh = open(path, "w")
    
    for employee_dep in employee_list:
        for employee in employee_dep:
            
            fh.write(employee + "\n")

    fh.close()

write_employees_to_file(employee_list, path)

    
