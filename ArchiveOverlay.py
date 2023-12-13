import os
import shutil
import sys
from tkinter import messagebox

import FileArchiveLib


def run_test():
    shutil.rmtree("C:\\temp\\archive\\Test\\", True)
    os.mkdir("C:\\temp\\archive\\Test\\")
    files = os.scandir("C:\\temp\\source\\ArchiveOverlayTest\\")
    for file in files:
        FileArchiveLib.ArchiveOverlay(file.path, "test")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        file_path = sys.argv[i]
        file_path = file_path.upper()
        if not file_path.endswith(".DWG"):
            messagebox.showerror(
                "Error", f"File '{sys.argv[i]}' is not an Autocad file."
            )
            continue
        FileArchiveLib.ArchiveOverlay(sys.argv[i], "ArchiveOverlay")
exit()
