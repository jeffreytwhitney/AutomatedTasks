import os
import shutil
import sys

import FileArchiveLib


def run_test():
    shutil.rmtree("C:\\temp\\archive\\Test\\", True)
    os.mkdir("C:\\temp\\archive\\Test\\")
    FileArchiveLib.CopyFileWithFileNameAppend("C:\\temp\\source\\ArchiveFileByExtensionTest\\1A.txt", "test", True)
    FileArchiveLib.CopyFileWithFileNameAppend("C:\\temp\\source\\ArchiveFileByExtensionTest\\1A.spp", "test", True)
    FileArchiveLib.CopyFileWithFileNameAppend("C:\\temp\\source\\ArchiveFileByExtensionTest\\1A.txt", "test", True)
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        FileArchiveLib.CopyFileWithFileNameAppend(sys.argv[i], "ArchiveFileByExtension", True)
exit()
