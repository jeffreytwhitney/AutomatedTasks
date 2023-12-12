import os
import shutil
import sys

import ArchiveLib
import FolderArchiveLib


def run_test():
    shutil.rmtree("C:\\temp\\archive\\Test\\", True)
    os.mkdir("C:\\temp\\archive\\Test\\")
    mv_sub_directory = ArchiveLib.GetMicroVuFolderSubDirectory("C:\\temp\\source\\ArchiveMicroVuFolderTest\\Pacing\\311\\M123456798")
    FolderArchiveLib.CopyFolderToSubDirectoryWithFileNameAppend("C:\\temp\\source\\ArchiveMicroVuFolderTest\\Pacing\\311\\M123456798", mv_sub_directory, "testwOutputPath")
    FolderArchiveLib.CopyFolderToSubDirectoryWithFileNameAppend("C:\\temp\\source\\ArchiveMicroVuFolderTest\\Pacing\\311\\M123456798", mv_sub_directory, "testwOutputPath")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:

    for i in range(1, n):
        sub_directory = ArchiveLib.GetMicroVuFolderSubDirectory(sys.argv[i])
        FolderArchiveLib.CopyFolderToSubDirectoryWithFileNameAppend(sys.argv[i], sub_directory, "ArchiveMicroVuFolder")
