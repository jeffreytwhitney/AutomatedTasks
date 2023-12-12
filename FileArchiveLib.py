import os
import shutil
from pathlib import WindowsPath
from tkinter import messagebox

import ArchiveLib


def CopyFile(file_path, ini_filename, show_messagebox=True):
    archive_file_path = ArchiveLib.GetFileOutputPath(file_path, ini_filename)
    if archive_file_path == "":
        return
    if os.path.exists(archive_file_path):
        if show_messagebox:
            messagebox.showerror("Error", f"File '{archive_file_path}' already exists.")
        return
    else:
        shutil.copy(file_path, archive_file_path)
        if show_messagebox:
            messagebox.showinfo("Success", f"File '{file_path}' has been copied to '{archive_file_path}'.")


def CopyFileWithOverwrite(file_path, ini_filename, show_messagebox=True):
    archive_filepath = ArchiveLib.GetFileOutputPath(file_path, ini_filename)
    if archive_filepath == "":
        return
    if os.path.exists(archive_filepath):
        if show_messagebox:
            user_response = messagebox.askyesno("Are You Sure?", f"File '{archive_filepath}' already exists. Overwrite?")
            if not user_response:
                return
            else:
                os.remove(archive_filepath)
    shutil.copy(file_path, archive_filepath)
    if show_messagebox:
        messagebox.showinfo("Success", f"File '{file_path}' has been copied to '{archive_filepath}'.")


def CopyFileWithFileNameAppend(current_filename, output_directory, show_messagebox=True):
    current_filepath = WindowsPath(current_filename)
    output_filepath = os.path.join(output_directory, current_filepath.name)

    if not os.path.exists(current_filename):
        if show_messagebox:
            messagebox.showerror("Error", f"File '{current_filename}' does not exist.")
        return

    if not os.path.exists(output_directory):
        try:
            os.makedirs(output_directory, exist_ok=True)
        except FileNotFoundError:
            if show_messagebox:
                messagebox.showerror("Error", f"Could not create directory '{output_directory}'.")
            return

    if not os.path.exists(output_filepath):
        shutil.copy(current_filename, output_filepath)
        if show_messagebox:
            messagebox.showinfo("Success", f"File '{current_filename}' has been copied to '{output_filepath}'.")
    else:
        stem_suffix = 1
        while True:
            file_stem = current_filepath.stem + "-" + str(stem_suffix)
            file_extension = current_filepath.suffix
            output_filename = file_stem + file_extension
            output_filepath = os.path.join(output_directory, output_filename)
            if os.path.exists(output_filepath):
                stem_suffix += 1
            else:
                shutil.copy(current_filename, output_filepath)
                if show_messagebox:
                    messagebox.showinfo("Success", f"File '{current_filename}' has been copied to '{output_filepath}'.")
                break
        return


def CopyMicroVuFile(source_filepath, ini_filename, show_messagebox=True):
    output_root_directory = ArchiveLib.GetFolderOutputPath(ini_filename)
    mv_subDirectory = ArchiveLib.GetMicroVuFileSubDirectory(source_filepath)
    output_directory = os.path.join(output_root_directory, mv_subDirectory)
    CopyFileWithFileNameAppend(source_filepath, output_directory, show_messagebox)


def GetIncrementedFileSuffix(file_suffix):
    return_value = chr(ord(file_suffix) + 1)
    if return_value == "[":
        return_value = "AA"
    return return_value


def GetIncrementedFilePath(source_filepath):
    source_path = WindowsPath(source_filepath)
    root_filename = source_path.stem[:len(source_path.stem) - 1]
    file_extension = source_path.suffix
    current_file_suffix = source_path.stem[-1]
    while True:
        incremented_file_suffix = GetIncrementedFileSuffix(current_file_suffix)
        incremented_filename = root_filename + incremented_file_suffix + file_extension
        incremented_filepath = source_path.with_name(incremented_filename)
        if not os.path.exists(incremented_filepath):
            return_path = incremented_filepath
            break
        else:
            current_file_suffix = incremented_file_suffix
    return return_path


def ArchiveOverlay(source_filepath, ini_filename):
    if WindowsPath(source_filepath).suffix.upper() != ".DWG":
        messagebox.showerror("Error", f"File '{source_filepath}' is not an overlay.")
        return

    archive_filepath = ArchiveLib.GetFileOutputPath(source_filepath, ini_filename)
    if archive_filepath == "":
        messagebox.showerror("Error", f"Could not retrieve archive filepath.")
        return

    incremented_filepath = GetIncrementedFilePath(source_filepath)
    if incremented_filepath == "":
        messagebox.showerror("Error", f"Could not retrieve incremented filepath.")
        return

    if os.path.exists(incremented_filepath):
        messagebox.showerror("Error", f"File '{incremented_filepath}' already exists.")
        return

    if os.path.exists(archive_filepath):
        user_response = messagebox.askyesno("Are You Sure?", f"Directory '{archive_filepath}' already exists. Overwrite?")
        if not user_response:
            return
    shutil.copy(source_filepath, archive_filepath)
    os.rename(source_filepath, incremented_filepath)
    source_filename = WindowsPath(source_filepath).name
    incremented_filename = WindowsPath(incremented_filepath).name
    archive_directory = os.path.dirname(archive_filepath)
    messagebox.showinfo("Success", f"Archived '{source_filename}' to '{str(archive_directory)}' and renamed file to '{incremented_filename}'")
    return
