import os


def FindFilePathByDirectoryName(root_paths: list[str], dir_name: str, file_name) -> str:
    for root_path in root_paths:
        test_path = os.path.join(root_path, dir_name, file_name)
        if os.path.exists(test_path):
            return test_path
    return ""


def UpdateExportLocationInMicroVu(file_path: str, old_path: str, new_path: str):
    with open(file_path, 'r', encoding='utf-16-le') as file_handle:
        file_string = file_handle.read()

    file_string = file_string.replace(old_path, new_path)
    file_string = file_string.replace(old_path, new_path)
    with open(file_path, 'w', encoding='utf-16-le') as file_handle:
        file_handle.write(file_string)


def UpdateArchiveReplaceMicroVus(archive_directories: list[str], input_directory: str, output_directory: str):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(".iwp"):
                print(file)

                file_path = os.path.join(root, file)
                directory_name = os.path.basename(os.path.dirname(file_path))
                output_path = FindFilePathByDirectoryName(archive_directories, directory_name, file)
                print(output_path)
                # UpdateExportLocationInMicroVu(file_path, "Z:\\", "C:\\MvDup\\Input")
                # FileArchiveLib.ArchiveMicroVuFile(file_path, "ArchiveMicroVuFolder", False)


untested_file_path = "V:\\Inspect Programs\\Micro-Vu\\1Factory_Untested\\311\\"
one_factory_path = "V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\311\\1Factory\\"
old_directories: list[str] = ["V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\311\\additive\\",
                              "V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\311\\ortho\\",
                              "V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\311\\pacing\\"]
UpdateArchiveReplaceMicroVus(old_directories, untested_file_path, one_factory_path)
