import os
import sys
import FolderArchiveLib
import shutil


def run_test():
    shutil.rmtree("C:\\temp\\archive\\Test\\", True)
    os.mkdir("C:\\temp\\archive\\Test\\")
    FolderArchiveLib.CopyFolderWithFileNameAppend("C:\\temp\\source\\CMMTest\\M123456798", "testwOutputPath", True)
    FolderArchiveLib.CopyFolderWithFileNameAppend("C:\\temp\\source\\CMMTest\\M123456798", "testwOutputPath")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        FolderArchiveLib.CopyFolderWithFileNameAppend(sys.argv[i], "ArchiveCMMFolder", True)
exit()

