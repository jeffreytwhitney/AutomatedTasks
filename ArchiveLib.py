import configparser
import os
import pathlib
from tkinter import filedialog


def GetFileOutputDirectory(source_file_path, ini_filename):
    file_extension = GetFileExtensionFromFilePath(source_file_path)
    archive_folder = GetStoredIniValue(
        "FileExtensionPaths", file_extension, ini_filename
    )
    if archive_folder == "":
        archive_folder = filedialog.askdirectory()
        if archive_folder != "":
            StoreIniValue(
                archive_folder, "FileExtensionPaths", file_extension, ini_filename
            )
    if archive_folder != "":
        return archive_folder


def GetFileOutputPath(source_file_path, ini_filename):
    file_extension = GetFileExtensionFromFilePath(source_file_path)
    archive_folder = GetStoredIniValue(
        "FileExtensionPaths", file_extension, ini_filename
    )
    if archive_folder == "":
        archive_folder = filedialog.askdirectory()
        if archive_folder != "":
            StoreIniValue(
                archive_folder, "FileExtensionPaths", file_extension, ini_filename
            )
    if archive_folder != "":
        archive_path = pathlib.Path.joinpath(
            pathlib.WindowsPath(archive_folder),
            pathlib.WindowsPath(source_file_path).name,
        )
        return archive_path
    else:
        return archive_folder


def GetMicroVuFileSubDirectory(directory_to_check):
    mv_directory = GetMicroVuFolderSubDirectory(directory_to_check)
    parts = pathlib.WindowsPath(directory_to_check).parts
    machine_type_idx = parts.index(mv_directory)
    program_idx = parts.index(mv_directory) + 2
    program_directory = parts[program_idx]
    machine_type_directory = parts[machine_type_idx]
    return_path = pathlib.Path(program_directory, machine_type_directory)
    return str(return_path)


def GetIniFilePath(ini_file_name):
    current_dir = os.path.dirname(__file__)
    ini_path = current_dir + "\\" + ini_file_name + ".ini"
    return ini_path


def GetStoredIniValue(ini_section, ini_key, ini_filename):
    ini_file_path = GetIniFilePath(ini_filename)
    config = configparser.ConfigParser()
    config.read(ini_file_path)
    try:
        config_value = config.get(ini_section, ini_key)
    except:
        try:
            config_value = config.get(ini_section, "*")
        except:
            config_value = ""
    return config_value


def StoreIniValue(ini_value, ini_section, ini_key, ini_filename):
    ini_file_path = GetIniFilePath(ini_filename)
    config = configparser.ConfigParser()
    if not os.path.exists(ini_file_path):
        config.add_section(ini_section)
        config.set(ini_section, ini_key, ini_value)
        with open(ini_file_path, "w") as conf:
            config.write(conf)
    else:
        if not config.has_section(ini_section):
            config.add_section(ini_section)
        config.read(ini_file_path)
        config.set(ini_section, ini_key, ini_value)
        with open(ini_file_path, "w") as conf:
            config.write(conf)


def GetFolderOutputPath(ini_filename):
    output_path = GetStoredIniValue("OutputFilePath", "Path", ini_filename)
    if output_path == "":
        output_path = filedialog.askdirectory()
        if output_path != "":
            StoreIniValue(output_path, "OutputFilePath", "Path", ini_filename)
    return output_path


def GetFileExtensionFromFilePath(source_file_path):
    return str(pathlib.WindowsPath(source_file_path).suffix.replace(".", ""))


def GetDirectoryFromFilePath(source_file_path):
    return os.path.dirname(source_file_path)


def GenerateFolderOutputPath(source_file_path, ini_filename):
    output_root_directory = GetFolderOutputPath(ini_filename)
    source_file_parent_folder = pathlib.WindowsPath(source_file_path).parts[-1]
    return str(
        pathlib.WindowsPath(output_root_directory).joinpath(source_file_parent_folder)
    )


def GetMicroVuFolderSubDirectory(directory_to_check):
    if directory_to_check.find("\\311\\") != -1:
        return "311"
    if directory_to_check.find("\\341\\") != -1:
        return "341"
    if directory_to_check.find("\\420\\") != -1:
        return "420"
