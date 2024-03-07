import os
import pathlib
import shutil
import sys
from tkinter import simpledialog

import pymsgbox

import ArchiveLib
import FolderArchiveLib
from lib.MicroVuProcessor import uprev_microvu


def run_test():
    shutil.rmtree("C:\\TEST\\AutomatedTasks\\Input\\", True)
    shutil.copytree("C:\\TEST\\AutomatedTasks\\Reset\\", "C:\\TEST\\AutomatedTasks\\Input\\")

    new_dir = get_new_directory_name("C:\\TEST\\AutomatedTasks\\Input\\300-029907-00 REV A\\", "A", "B")
    os.rename("C:\\TEST\\AutomatedTasks\\Input\\300-029907-00 REV A\\", new_dir)
    for mvfile in os.listdir(new_dir):
        new_path = str(os.path.join(new_dir, mvfile))
        uprev_microvu(new_path, "A", "B")
    return


def get_new_directory_name(dir_path: str, old_rev: str, new_rev: str) -> str:
    dir_path = dir_path.upper()
    current_directory_name: str = pathlib.Path(dir_path).parts[-1].upper()

    if "REV" not in current_directory_name:
        return dir_path
    if current_directory_name.count("REV") > 1:
        pymsgbox.alert("Directory has the letters 'REV' in it more than once, so I don't know what to change.")
        return ""

    new_directory_name = current_directory_name

    search_string = f"REV{old_rev.upper()}"
    if search_string in current_directory_name:
        new_directory_name = current_directory_name.replace(search_string, f"REV_{new_rev}")

    search_string = f"REV {old_rev.upper()}"
    if search_string in current_directory_name:
        new_directory_name = current_directory_name.replace(search_string, f"REV_{new_rev}")

    search_string = f"REV_{old_rev.upper()}"
    if search_string in current_directory_name:
        new_directory_name = current_directory_name.replace(search_string, f"REV_{new_rev}")

    return dir_path.replace(current_directory_name, new_directory_name)


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        dir_path = sys.argv[i]
        old_rev_name = simpledialog.askstring("Old Rev", "Enter Old Rev:")
        new_rev_name = simpledialog.askstring("New Rev", "Enter NEW Rev:")
        new_dir_path = get_new_directory_name(dir_path, old_rev_name, new_rev_name)
        sub_directory = ArchiveLib.GetMicroVuFolderSubDirectory(dir_path)
        FolderArchiveLib.CopyFolderToSubDirectoryWithFileNameAppend(dir_path, sub_directory, "ArchiveMicroVuFolder", False)
        os.rename(dir_path, new_dir_path)
        for file in os.listdir(new_dir_path):
            new_file = str(os.path.join(new_dir_path, file))
            uprev_microvu(new_file, old_rev_name, new_rev_name)

exit()
