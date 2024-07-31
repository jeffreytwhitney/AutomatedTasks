import os
import sys
from tkinter import messagebox

import ArchiveLib


def run_test():
    sub_directory = ArchiveLib.GetMicroVuFolderSubDirectory("X:\\Quality Calibration\\Work in Progress\\Jeffrey\\1Factory Conversion\\311\\JP100153081_REV C")
    dirname = \
        os.path.dirname("X:\\Quality Calibration\\Work in Progress\\Jeffrey\\1Factory Conversion\\311\\JP100153081_REV C\\").split("\\")[
            -1]
    messagebox.showinfo("Hi!", dirname)
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:

    for i in range(1, n):
        machine_directory = ArchiveLib.GetMicroVuFolderSubDirectory(sys.argv[i])
        output_directory = ""
        dirname = os.path.dirname(sys.argv[i]).split("\\")[-1]
        messagebox.showinfo("Hi!", dirname)

        # if machine_directory == "311":
        #     dirname = os.path.dirname(sys.argv[i])

        # if os.path.exists(output_directory):
        #     if user_response := messagebox.askyesno("Are You Sure?", f"Directory '{output_directory}' already exists. Overwrite?"):
        #         shutil.rmtree(output_directory)
        #     else:
        #         exit()
        # shutil.copytree(source_directory, output_directory)

        exit()
