from tkinter import messagebox

import RunPowershell

RunPowershell.run_powershell_script("C:\\Users\\Public\\CURL\\bin\\CMM.ps1")

messagebox.showinfo("Hello", f"Hi!")
