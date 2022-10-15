from pathlib import Path
import sys, os
import shutil


folder_sort = Path(sys.argv[1])

types_file = {"archives": ('ZIP', 'GZ', 'TAR', 'RAR'),
              "documents": ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
              "audio": ('MP3', 'OGG', 'WAV', 'AMR'),
              "images": ('JPEG', 'PNG', 'JPG', 'SVG'),
              "video": ('AVI', 'MP4', 'MOV', 'MKV'),
              "unknown_type_file": ""}

upper_case_letters = {  'А': 'A',
                        'Б': 'B',
                        'В': 'V',
                        'Г': 'G',
                        'Д': 'D',
                        'Е': 'E',
                        'Ё': 'E',
                        'Ж': 'Zh',
                        'З': 'Z',
                        'И': 'I',
                        'І': 'I',
                        'Ї': 'YI',
                        'Й': 'Y',
                        'К': 'K',
                        'Л': 'L',
                        'М': 'M',
                        'Н': 'N',
                        'О': 'O',
                        'П': 'P',
                        'Р': 'R',
                        'С': 'S',
                        'Т': 'T',
                        'У': 'U',
                        'Ф': 'F',
                        'Х': 'H',
                        'Ц': 'Ts',
                        'Ч': 'Ch',
                        'Ш': 'Sh',
                        'Щ': 'Sch',
                        'Ъ': '',
                        'Ы': 'Y',
                        'Ь': '',
                        'Э': 'E',
                        'Ю': 'Yu',
                        'Я': 'Ya'}

lower_case_letters = {  'а': 'a',
                        'б': 'b',
                        'в': 'v',
                        'г': 'g',
                        'д': 'd',
                        'е': 'e',
                        'ё': 'e',
                        'ж': 'zh',
                        'з': 'z',
                        'и': 'i',
                        'і': 'i',
                        'ї': 'yi',
                        'й': 'y',
                        'к': 'k',
                        'л': 'l',
                        'м': 'm',
                        'н': 'n',
                        'о': 'o',
                        'п': 'p',
                        'р': 'r',
                        'с': 's',
                        'т': 't',
                        'у': 'u',
                        'ф': 'f',
                        'х': 'h',
                        'ц': 'ts',
                        'ч': 'ch',
                        'ш': 'sh',
                        'щ': 'sch',
                        'ъ': '',
                        'ы': 'y',
                        'ь': '',
                        'э': 'e',
                        'ю': 'yu',
                        'я': 'ya'}


def create_folders():

    for name_type_file in types_file:
        name_type_folder = Path(f"{folder_sort}/{name_type_file}")
        
        if not name_type_folder.exists():
            os.mkdir(name_type_folder)
            print(f"Create {name_type_folder}")

def find_type_file(file):

    for name_type_file, type_file in types_file.items():              

        if file.suffix[1:].upper() in type_file:
            return name_type_file

    return "unknown_type_file"

def move_file(file, new_name, type_file):
  
    move_path = Path(f"{folder_sort}/{type_file}")

    if Path(f"{move_path}/{file.name}").exists():
        print(f"{move_path}/{file.name} already exists")
    
    else:
        shutil.move(file, f"{move_path}/{new_name}{file.suffix}")
        print(f"{file} moved to {move_path}/{new_name}{file.suffix}")

def normalize(name_file):

    normalize_name = ""

    for char in name_file:

        if char in upper_case_letters:
            char = upper_case_letters[char]

        elif char in lower_case_letters:
            char = lower_case_letters[char]
        
        elif not char.isdigit() and not char.isalpha():
            char = "_"

        normalize_name += char

    return normalize_name

def sort_file_in_folder(folder):    

    for element in folder.iterdir():

        if element.is_dir():
            if element.name in types_file:
                continue

            new_name = normalize(element.name)
            print(f"{element} rename by {new_name}")
            element = Path(shutil.move(element, f"{element.parent}/{new_name}")) 
            sort_file_in_folder(element)

        else:

            name_file = element.name.removesuffix(element.suffix)
            new_name = normalize(name_file)
            type_file = find_type_file(element)
            move_file(element, new_name, type_file)
    

if __name__ == "__main__":

    create_folders()
    sort_file_in_folder(folder_sort)
    print("Done")
