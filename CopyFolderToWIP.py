import os
import sys
import FolderArchiveLib
import shutil


def run_test():
    shutil.rmtree("C:\\temp\\archive\\Test\\", True)
    os.mkdir("C:\\temp\\archive\\Test\\")
    FolderArchiveLib.CopyFolderWithOverwrite("C:\\temp\\source\\CopyToWIPTest\\M123456798", "testwOutputPath")
    FolderArchiveLib.CopyFolderWithOverwrite("C:\\temp\\source\\CopyToWIPTest\\M123456798", "testwOutputPath")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        FolderArchiveLib.CopyFolderWithOverwrite(sys.argv[i], "CopyFolderToWIP")
exit()

