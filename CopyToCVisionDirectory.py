import os
import pathlib
import shutil
import sys
from tkinter import messagebox

n = len(sys.argv)

if n != 1:
    output_directory = ""
    for i in range(1, n):
        if pathlib.Path(sys.argv[i]).suffix.upper() != ".DXF":
            messagebox.showinfo("Dumbass!", f"'{sys.argv[i]}' is not a .DXF file.")
            exit()
        file_name = os.path.basename(sys.argv[i])
        output_path = f"V:\\Inspect Programs\\C-Vision\\Active DXF's\\{file_name}"

        if os.path.exists(output_path):
            if user_response := messagebox.askyesno("Are You Sure?", f"File '{output_path}' already exists. Overwrite?"):
                os.remove(output_path)
            else:
                continue
        shutil.copy(sys.argv[i], output_path)
