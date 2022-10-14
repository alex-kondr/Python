import sys
from pathlib import Path
import shutil


sort_folder = Path(sys.argv[1])

picture_file = ('JPEG', 'PNG', 'JPG', 'SVG')
video_file = ('AVI', 'MP4', 'MOV', 'MKV')
doc_file = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
music_file = ('MP3', 'OGG', 'WAV', 'AMR')
arhive_file = ('ZIP', 'GZ', 'TAR')


def sort_file_in_folder(sort_folder):
    for element in sort_folder.iterdir():
        if element.is_dir():
            # print(f"Folder name is {element.name}")
            sort_file_in_folder(element)
        else:
            # print(f"File suffix is {element.suffix}")

            if element.suffix[1:].upper() in picture_file:
                print(f"This is picture file: {element.name}")
                shutil.move(element, f"{sort_folder}/Котики/")
            elif element.suffix[1:].upper() in doc_file:
                print(f"This is doc file: {element.name}")
            elif element.suffix[1:].upper() in video_file:
                print(f"This is video file: {element.name}")
            elif element.suffix[1:].upper() in music_file:
                print(f"This is music file: {element.name}")
            elif element.suffix[1:].upper() in arhive_file:
                print(f"This is arhive file: {element.name}")
            else:
                print(f"Unsorted file: {element.name}")



sort_file_in_folder(sort_folder)
