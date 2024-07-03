import os
import re

import FileArchiveLib

pattern = re.compile(r"C:\\Users\\Public\\CURL\\in\\", re.IGNORECASE)

for root, dirs, files in os.walk("V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\311\\1Factory"):
    for file in files:
        if file.lower().endswith(".iwp"):
            print(file)

            file_path = os.path.join(root, file)
            FileArchiveLib.ArchiveMicroVuFile(file_path, "ArchiveMicroVuFolder", False)

            with open(file_path, 'r', encoding='utf-16-le') as file_handle:
                file_string = file_handle.read()

            match = pattern.sub(r"Z:\\", file_string)

            with open(file_path, 'w', encoding='utf-16-le') as file_handle:
                file_handle.write(match)

# for root, dirs, files in os.walk("V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\341\\1Factory"):
#     for file in files:
#         if file.lower().endswith(".iwp"):
#             print(file)
#
#             file_path = os.path.join(root, file)
#             FileArchiveLib.ArchiveMicroVuFile(file_path, "ArchiveMicroVuFolder", False)
#
#             with open(file_path, 'r', encoding='utf-16-le') as file_handle:
#                 file_string = file_handle.read()
#
#             file_string = file_string.replace("C:\\Users\\Public\\CURL\\in\\", "Z:\\")
#             file_string = file_string.replace("C:\\USERS\\PUBLIC\\CURL\\IN\\", "Z:\\")
#             with open(file_path, 'w', encoding='utf-16-le') as file_handle:
#                 file_handle.write(file_string)
#
# for root, dirs, files in os.walk("V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\420\\1Factory"):
#     for file in files:
#         if file.lower().endswith(".iwp"):
#             print(file)
#
#             file_path = os.path.join(root, file)
#             FileArchiveLib.ArchiveMicroVuFile(file_path, "ArchiveMicroVuFolder", False)
#
#             with open(file_path, 'r', encoding='utf-16-le') as file_handle:
#                 file_string = file_handle.read()
#
#             file_string = file_string.replace("C:\\Users\\Public\\CURL\\in\\", "Z:\\")
#             file_string = file_string.replace("C:\\USERS\\PUBLIC\\CURL\\IN\\", "Z:\\")
#
#             with open(file_path, 'w', encoding='utf-16-le') as file_handle:
#                 file_handle.write(file_string)
