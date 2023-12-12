import os
import pathlib
import shutil
import ArchiveLib
from tkinter import messagebox
import FileArchiveLib


def CopyFolderToSubDirectoryWithFileNameAppend(source_directory, sub_directory, ini_file_name):
    output_directory = ArchiveLib.GenerateFolderOutputPath(source_directory, ini_file_name)
    if output_directory == "":
        return
    output_subdirectory = os.path.join(output_directory, sub_directory)
    for file in os.scandir(source_directory):
        if file.is_file():
            FileArchiveLib.CopyFileWithFileNameAppend(current_filename=file.path, output_directory=output_subdirectory, show_messagebox=False)
    messagebox.showinfo("Success", f"Folder '{source_directory}' has been copied to '{output_subdirectory}'.")
    return


def CopyFolderWithFileNameAppend(source_directory, ini_file_name, show_messagebox=True, recurse=False):
    output_directory = ArchiveLib.GenerateFolderOutputPath(source_directory, ini_file_name)
    if output_directory == "":
        return
    for item in os.scandir(source_directory):
        if item.is_file():
            FileArchiveLib.CopyFileWithFileNameAppend(current_filename=item.path, output_directory=output_directory, show_messagebox=False)
        if recurse:
            if item.is_dir:
                CopyFolderWithFileNameAppend(item.path, ini_file_name, False, True)
    if show_messagebox:
        messagebox.showinfo("Success", f"Folder '{source_directory}' has been copied to '{output_directory}'.")
    return


def CopyFolderWithOverwrite(source_directory, ini_file_name):
    output_directory = ArchiveLib.GenerateFolderOutputPath(source_directory, ini_file_name)
    if output_directory == "":
        return
    if os.path.exists(output_directory):
        user_response = messagebox.askyesno("Are You Sure?", f"Directory '{output_directory}' already exists. Overwrite?")
        if not user_response:
            return
        else:
            shutil.rmtree(output_directory)
    shutil.copytree(source_directory, output_directory)
    messagebox.showinfo("Success", f"Folder '{source_directory}' has been copied to '{output_directory}'.")
    return


def CopyFolder(source_directory, ini_file_name):
    output_directory = ArchiveLib.GenerateFolderOutputPath(source_directory, ini_file_name)
    if output_directory == "":
        return
    if os.path.exists(output_directory):
        messagebox.showerror("Error", f"Folder '{source_directory}' already exists.")
    else:
        shutil.copytree(source_directory, output_directory)
        messagebox.showinfo("Success", f"Folder '{source_directory}' has been copied to '{output_directory}'.")
    return
