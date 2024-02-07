import os
import shutil
import sys

from lib.MicroVuProcessor import process_file


def run_test():
    shutil.rmtree("C:\\TEST\\AutomatedTasks\\Input\\", True)
    os.mkdir("C:\\TEST\\AutomatedTasks\\Input\\")
    shutil.copy(
        "C:\\TEST\\AutomatedTasks\\Reset\\10873 Housing.iwp",
        "C:\\TEST\\AutomatedTasks\\Input\\10873 Housing.iwp",
    )
    process_file("C:\\TEST\\AutomatedTasks\\Input\\10873 Housing.iwp")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        file_path = sys.argv[i]
        process_file(file_path)
exit()
