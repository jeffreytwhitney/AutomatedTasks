import os
import os.path
import shutil

import FileArchiveLib


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


def UpdateArchiveReplaceMicroVus(archive_directories: list[str], input_directory: str, one_factory_rootpath: str):
    for root, dirs, files in os.walk(input_directory):
        for file in files:
            if file.lower().endswith(".iwp"):
                print(file)

                input_file_path = os.path.join(root, file)
                directory_name = os.path.basename(os.path.dirname(input_file_path))
                if archive_filepath := FindFilePathByDirectoryName(archive_directories, directory_name, file):
                    FileArchiveLib.ArchiveMicroVuFile(archive_filepath, "ArchiveMicroVuFolder", False)
                    os.remove(archive_filepath)
                    if not os.listdir(os.path.dirname(archive_filepath)):
                        os.rmdir(os.path.dirname(archive_filepath))
                    output_directory = os.path.join(one_factory_rootpath, directory_name)
                    if not os.path.isdir(output_directory):
                        os.mkdir(output_directory)
                    output_filepath = os.path.join(output_directory, file)
                    if os.path.isfile(output_filepath):
                        os.remove(input_file_path)
                    shutil.move(input_file_path, output_filepath)
                    if not os.listdir(os.path.dirname(input_file_path)):
                        os.rmdir(os.path.dirname(input_file_path))


untested_file_path = "V:\\Inspect Programs\\Micro-Vu\\1Factory_Untested\\420\\"
one_factory_path = "V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\420\\1Factory\\"
old_directories: list[str] = ["V:\\Inspect Programs\\Micro-Vu\\Approved Programs\\420\\ortho\\"]
UpdateArchiveReplaceMicroVus(old_directories, untested_file_path, one_factory_path)
