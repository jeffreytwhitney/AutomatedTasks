import os
import shutil
import sys
from tkinter import messagebox

import FileArchiveLib


def run_test():
    shutil.rmtree("C:\\temp\\archive\\Test\\", True)
    os.mkdir("C:\\temp\\archive\\Test\\")
    FileArchiveLib.ArchiveMicroVuFile("C:\\temp\\source\\ArchiveMicroVuFileTest\\Pacing\\311\\M123456798\\3a.iwp", "testwOutputPath", True)
    FileArchiveLib.ArchiveMicroVuFile("C:\\temp\\source\\ArchiveMicroVuFileTest\\Pacing\\311\\M123456798\\3a.iwp", "testwOutputPath", True)
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        file_path = sys.argv[i]
        file_path = file_path.upper()
        if not file_path.endswith(".IWP"):
            messagebox.showerror("Error", f"File '{sys.argv[i]}' is not a MicroVu file.")
            continue
        FileArchiveLib.ArchiveMicroVuFile(sys.argv[i], "ArchiveMicroVuFolder", True)
exit()
