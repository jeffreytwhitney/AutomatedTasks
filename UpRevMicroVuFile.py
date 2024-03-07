import shutil
import sys
from tkinter import simpledialog

import FileArchiveLib
from lib.MicroVuProcessor import uprev_microvu


def run_test():
    shutil.rmtree("C:\\TEST\\AutomatedTasks\\Input\\", True)
    shutil.copytree("C:\\TEST\\AutomatedTasks\\Reset\\", "C:\\TEST\\AutomatedTasks\\Input\\")
    FileArchiveLib.ArchiveMicroVuFile("C:\\TEST\\AutomatedTasks\\Reset\\311\\Pacing\\TEST REV_A\\TEST SIDE.iwp", "ArchiveMicroVuFolder", False)
    uprev_microvu("C:\\TEST\\AutomatedTasks\\Reset\\311\\Pacing\\TEST REV_A\\TEST SIDE.iwp", "A", "B")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    old_rev_name = simpledialog.askstring("Old Rev", "Enter Old Rev:")
    new_rev_name = simpledialog.askstring("New Rev", "Enter NEW Rev:")
    for i in range(1, n):
        new_file = sys.argv[i]
        FileArchiveLib.ArchiveMicroVuFile(new_file, "ArchiveMicroVuFolder", False)
        uprev_microvu(new_file, old_rev_name, new_rev_name)

exit()
