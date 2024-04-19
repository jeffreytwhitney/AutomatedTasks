import os
import sys
from tkinter import simpledialog

from lib.MicroVuProcessor import uprev_cmm_filename


def run_test():
    # shutil.rmtree("C:\\TEST\\AutomatedTasks\\Input\\", True)
    # shutil.copytree("C:\\TEST\\AutomatedTasks\\Reset\\", "C:\\TEST\\AutomatedTasks\\Input\\")
    # FileArchiveLib.ArchiveMicroVuFile("C:\\TEST\\AutomatedTasks\\Reset\\311\\Pacing\\TEST SIDE.iwp", "ArchiveMicroVuFolder", False)
    # uprev_microvu("C:\\TEST\\AutomatedTasks\\Input\\311\\Pacing\\M956750A001 LENGTH- 1PART.iwp", "D", "E")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    old_rev_name = simpledialog.askstring("Old Rev", "Enter Old Rev:")
    new_rev_name = simpledialog.askstring("New Rev", "Enter NEW Rev:")
    for i in range(1, n):
        new_file = sys.argv[i]
        uprev_cmm_filename(new_file, old_rev_name, new_rev_name)
    for i in range(1, n):
        dir_path = sys.argv[i]
        for file in os.listdir(dir_path):
            new_file = str(os.path.join(dir_path, file))
            uprev_cmm_filename(new_file, old_rev_name, new_rev_name)
exit()
