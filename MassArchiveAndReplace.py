import os

import FileArchiveLib

for root, dirs, files in os.walk("C:\\TEST\\UpdateExport\\Input"):
    for file in files:
        if file.lower().endswith(".iwp"):
            print(file)

            file_path = os.path.join(root, file)
            FileArchiveLib.ArchiveMicroVuFile(file_path, "testwOutputPath", False)

            with open(file_path, 'r', encoding='utf-16-le') as file_handle:
                file_string = file_handle.read()

            file_string = file_string.replace("C:\\Users\\Public\\CURL\\in\\", "E:\\MicroVu\\")

            with open(file_path, 'w', encoding='utf-16-le') as file_handle:
                file_handle.write(file_string)
