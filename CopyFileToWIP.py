import os
import shutil
import sys

import FileArchiveLib


def run_test():
    shutil.rmtree("C:\\temp\\archive\\Test\\", True)
    os.mkdir("C:\\temp\\archive\\Test\\")
    FileArchiveLib.CopyFileWithOverwrite(
        "C:\\temp\\source\\CopyToWIPTest\\M123456798\\1C.txt", "test"
    )
    FileArchiveLib.CopyFileWithOverwrite(
        "C:\\temp\\source\\CopyToWIPTest\\M123456798\\1C.txt", "test"
    )
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        file_path = sys.argv[i]
        FileArchiveLib.CopyFileWithOverwrite(file_path, "CopyFileToWIP")
exit()
