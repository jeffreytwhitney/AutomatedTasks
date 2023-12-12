import os.path
import pathlib
import shutil
import sys
from tkinter import messagebox


def GetP2XFile(source_filepath):
    if pathlib.WindowsPath(source_filepath).suffix.upper() != ".PRG":
        messagebox.showerror("Error", f"File '{source_filepath}' is not a PC-DMIS file.")
        return
    output_filepath = str(pathlib.WindowsPath(source_filepath).with_suffix(".P2X"))
    if os.path.exists(output_filepath):
        return
    shutil.copy("X:\\Quality Calibration\\Work in Progress\\Jeffrey\\2020 R2 CMM Program Templates\\1 Factory Templates\\Sample.P2X", output_filepath)
    return


def run_test():
    GetP2XFile("C:\\temp\\source\\GetP2XFileTest\\Test.PRG")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        GetP2XFile(sys.argv[i])
exit()
