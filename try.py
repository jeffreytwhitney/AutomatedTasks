import winreg as wrg
from tkinter import messagebox

import admin

admin.elevate(True, True)

location = wrg.HKEY_CURRENT_USER

probe_key = wrg.OpenKeyEx(location, r"SOFTWARE\\Hexagon\\PC-DMIS\\2020 R2\\Option")
value_1 = wrg.QueryValueEx(probe_key, "LoadProbeUserSearchDirectory")

try:
    wrg.SetValueEx(probe_key, "LoadProbeUserSearchDirectory", 0, wrg.REG_SZ, "C:\\Users\\Public\\Documents\\Hexagon\\PC-DMIS\\2020 R2\\Probe Files\\Pacing\\TIGO\\Probe files\\")
except PermissionError:
    print("No permission")

if probe_key:
    wrg.CloseKey(probe_key)

print(value_1)
messagebox.showinfo("Hello", f"Hi!")
