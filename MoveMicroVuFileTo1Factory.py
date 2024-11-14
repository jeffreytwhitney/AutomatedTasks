import os
import shutil
import sys
from tkinter import messagebox

import ArchiveLib
import FileArchiveLib


def move_file_to_1Factory(input_filepath: str):
    if not os.path.isfile(input_filepath):
        return
    machine_directory = ArchiveLib.GetMicroVuFolderSubDirectory(input_filepath)
    file_name = os.path.basename(input_filepath)
    dirname = os.path.basename(os.path.dirname(input_filepath))
    output_directory = f"V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\{machine_directory}\\1Factory\\{dirname}"
    output_filepath = f"V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\{machine_directory}\\1Factory\\{dirname}\\{file_name}"

    if os.path.exists(output_filepath):
        if not (
                _ := messagebox.askyesno(
                    "Are You Sure?",
                    f"Directory '{output_filepath}' already exists. Archive and overwrite?",
                )
        ):
            return
        FileArchiveLib.ArchiveMicroVuFile(input_filepath, "ArchiveMicroVuFolder", False)
        os.remove(output_filepath)

    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    shutil.move(input_filepath, output_filepath)


n = len(sys.argv)

if n > 1:

    for i in range(1, n):
        move_file_to_1Factory(sys.argv[i])
