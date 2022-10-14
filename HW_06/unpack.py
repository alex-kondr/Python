import shutil
from pathlib import Path

archive_path = Path("backup_folder.zip")
path_to_unpack = Path("HW_06/111")

def unpack(archive_path, path_to_unpack):

    shutil.unpack_archive(archive_path, path_to_unpack)


unpack(archive_path, path_to_unpack)
