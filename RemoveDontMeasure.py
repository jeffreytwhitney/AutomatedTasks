import shutil
import sys

from lib.MicroVuProcessor import remove_dont_measure_statements


def run_test():
    shutil.rmtree("C:\\TEST\\AutomatedTasks\\Input\\", True)
    shutil.copytree("C:\\TEST\\AutomatedTasks\\Reset\\", "C:\\TEST\\AutomatedTasks\\Input\\")
    remove_dont_measure_statements("C:\\TEST\\AutomatedTasks\\Input\\C18665-18.iwp")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        new_file = sys.argv[i]
        remove_dont_measure_statements(new_file)
exit()
