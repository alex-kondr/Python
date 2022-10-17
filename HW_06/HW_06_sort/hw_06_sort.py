import shutil, sys
from pathlib import Path
from translit_letters import *

   
folder_sort = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("*")

types_file = {"archives": ('ZIP', 'GZ', 'TAR'),
              "documents": ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'),
              "audio": ('MP3', 'OGG', 'WAV', 'AMR'),
              "images": ('JPEG', 'PNG', 'JPG', 'SVG'),
              "video": ('AVI', 'MP4', 'MOV', 'MKV')}

def create_folders() -> dict:
    """Creates folders on type"""

    dict_on_type = {"unknown_type_file": []}

    for name_type_file in types_file:

        name_type_folder = folder_sort.joinpath(name_type_file)
        dict_on_type.update({name_type_file: []})
        name_type_folder.mkdir(exist_ok=True)
        print(f"Create {name_type_folder}")

    return dict_on_type

def find_type_file(file: Path) -> str:
    """Finds the file type and returns its name"""

    for name_type_file, type_file in types_file.items():

        if file.suffix[1:].upper() in type_file:
            return name_type_file

    return "unknown_type_file"


def move_file(file: Path, new_name: str, type_file: str) -> Path:
    """Moving file on its type and rename on [new_name]"""

    move_path = folder_sort.joinpath(type_file)

    if move_path.joinpath(file.name).exists():
        print(f"{move_path.joinpath(file.name)} already exists")

    elif type_file == "archives":
        new_file = file
        shutil.unpack_archive(file, move_path.joinpath(just_name_file(file)))
        print(f"Unpack {file} to {type_file}")

    else:
        new_file = file.rename(move_path.joinpath(new_name + file.suffix))
        print(f"{file} moved to {new_file}")

    return new_file

def just_name_file(file: str) -> str:
    name = file.name.removesuffix(file.suffix)
    return name

def main():
    unknown_extensions = []

    list_file_on_type = create_folders()
    list_file_on_type, unknown_extensions = sort_file_in_folder(folder_sort, 
                                                                list_file_on_type, 
                                                                unknown_extensions)

    list_of_extensions = {"known_type": [],
                          "unknown_type": set(unknown_extensions)}

    for extensions in types_file.values():
        list_of_extensions['known_type'] += extensions

    rm_empty_dir(folder_sort)
    print("Deleted empty folders")

    print(f"list_file_on_type: {list_file_on_type}")
    print(f"list_of_extensions: {list_of_extensions}")
    print("Done")


def normalize(name_file: str) -> str:
    """Normalize name file"""

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

def rm_empty_dir(dir: Path):

    for element in dir.iterdir():
        if element.is_dir():
            try:
                element.rmdir()
                print(f"Deleted folder {element}")
            except OSError:
                rm_empty_dir(element)


def sort_file_in_folder(folder: Path, list_file_on_type: dict, unknown_extensions: list):
    """Sortes files on its type on folder and unpack archives"""
    
    for element in folder.iterdir():

        if element.is_dir():
            if element.name in types_file:
                continue

            new_name = normalize(element.name)
            print(f"{element} rename by {new_name}")
            element = element.rename(element.parent.joinpath(new_name))
            sort_file_in_folder(element, list_file_on_type, unknown_extensions)

        else:

            name_file = just_name_file(element)
            new_name = normalize(name_file)
            type_file = find_type_file(element)

            if type_file == "unknown_type_file":
                unknown_extensions.append(element.suffix[1:])
                new_file = element
            else:
                new_file = move_file(element, new_name, type_file)

            list_file_on_type[type_file].append(new_file.name)

    return list_file_on_type, unknown_extensions


if __name__ == "__main__":

    if folder_sort.is_dir():
        main()
    else:
        print("Enter valid folder")
