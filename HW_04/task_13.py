from pathlib import Path

def parse_folder(path):

    files = []
    folders = []

    for path_iter in path.iterdir():

        if path_iter.is_file():
            files.append(path_iter.name)

        elif path_iter.is_dir():
            folders.append(path_iter.name)

    return files, folders
