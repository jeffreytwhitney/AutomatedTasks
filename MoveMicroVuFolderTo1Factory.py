import os
import shutil
import sys
from tkinter import messagebox

import ArchiveLib
import FolderArchiveLib


def run_test():
    dir_text = "X:\\Quality Calibration\\Work in Progress\\Jeffrey\\1Factory Conversion\\311\\JP100153081_REV C"
    dir_name = os.path.basename(dir_text)
    messagebox.showinfo("Hi!", dir_name)
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    output_directory = ""
    for i in range(1, n):
        machine_directory = ArchiveLib.GetMicroVuFolderSubDirectory(sys.argv[i])
        dirname = os.path.basename(sys.argv[i])

        output_directory = f"V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\{machine_directory}\\1Factory\\{dirname}"
        if os.path.exists(output_directory):
            if user_response := messagebox.askyesno("Are You Sure?", f"Directory '{output_directory}' already exists. Archive and overwrite?"):
                FolderArchiveLib.CopyFolderToSubDirectoryWithFileNameAppend(
                    output_directory, machine_directory, "ArchiveMicroVuFolder", False)
                shutil.rmtree(output_directory)
            else:
                continue
        shutil.copytree(sys.argv[i], output_directory)
        shutil.rmtree(sys.argv[i])
