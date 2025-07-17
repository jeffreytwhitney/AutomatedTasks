import os
import shutil
import sys

import ArchiveLib
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
        output_root_directory = ArchiveLib.GetFileOutputDirectory(sys.argv[i], "ArchiveFileByExtension")
        FileArchiveLib.CopyFileWithFileNameAppend(sys.argv[i], output_root_directory, True)
        
exit()
