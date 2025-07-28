import os
import shutil
from pathlib import Path

import win32com.client

copy_root_path = "C:\\pcdmis-temp\\"


def copy_program_to_temp_location(file_path_to_copy) -> str:
    path = Path(file_path_to_copy)
    subdirectory = path.name
    output_path = str(path.joinpath(copy_root_path, subdirectory))
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    shutil.copytree(file_path_to_copy, output_path)
    return output_path


def up_rev_local_copy(file_path_to_edit, ):
    pcdmis = win32com.client.Dispatch("PCDLRN.Application")
    pcdmis.Visible = False

    if pcdmis is not None:
        version = pcdmis.VersionString
        print(f"Current PC-DMIS Version: {version}")

        #command.IsComment

        #comment_command = DmisCommand.OptionProbeCommand


file_path = "X:\\Quality Calibration\\Work in Progress\\Jeffrey\\49-20-01-4 1Factory\\"
directory = Path("path/to/your/folder")

for file in directory.rglob("*.prg"):
    print(file)
