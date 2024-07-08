import os.path
import pathlib
import shutil
import sys


def GetP2XFolder(source_filepath):
    for root, dirs, files in os.walk(source_filepath):
        for file in files:
            if file.upper().endswith(".PRG"):
                input_filepath = str(os.path.join(root, file))
                output_filepath = str(pathlib.WindowsPath(input_filepath).with_suffix(".P2X"))
                if os.path.exists(output_filepath):
                    continue
                else:
                    shutil.copy(
                        "X:\\Quality Calibration\\Work in Progress\\Jeffrey\\2020 R2 CMM Program Templates\\1 Factory Templates\\Sample.P2X",
                        output_filepath,
                    )
    return


def run_test():
    GetP2XFolder("C:\\temp\\source\\GetP2XFileTest\\")
    return


n = len(sys.argv)

if n == 1:
    run_test()
else:
    for i in range(1, n):
        GetP2XFolder(sys.argv[i])
exit()
