import os
import pathlib
import shutil
import sys
from tkinter import messagebox

import FileArchiveLib


def run_test():
    shutil.rmtree("C:\\temp\\archive\\Test\\", True)
    os.mkdir("C:\\temp\\archive\\Test\\")
    FileArchiveLib.ArchiveOverlay("C:\\temp\\source\\ArchiveOverlayTest\\1A.dwg", "test")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        if pathlib.WindowsPath(sys.argv[i]).suffix.upper != ".DWG":
            messagebox.showerror("Error", f"File '{sys.argv[i]}' is not an Autocad file.")
            continue
        FileArchiveLib.ArchiveOverlay(sys.argv[i], "ArchiveOverlay")
exit()
