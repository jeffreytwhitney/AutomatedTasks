import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

import pyautogui
import pywinauto


def click_main_menu_gage_entry():
    for win in main_window.descendants():
        wintext = win.window_text()
        if wintext == "Main Menu":
            rect = win.rectangle()
            click_left = rect.left + 335
            click_top = rect.top + 120

            pyautogui.click(click_left, click_top)


Tk().withdraw()
if filename := askopenfilename(
        initialdir="X:\\Quality Calibration\\Work in Progress\\Jeffrey",
        filetypes=[("CSV files", "*.csv")],
):
    file_lines: list[str] = []

    with open(filename, "r+", encoding='utf-8') as file1:
        file_lines = file1.readlines()

app = pywinauto.application.Application().connect(title="GAGEtrak 6.8", class_name="OMain")
main_window = app.window(title="GAGEtrak 6.8", class_name="OMain")
main_window.set_focus()

for line in file_lines:
    overlay_name = line.split(",")[0]
    cvision_name = line.split(",")[1]
    click_main_menu_gage_entry()
    time.sleep(4)
    pyautogui.click(342, 59)
    time.sleep(4)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.typewrite(overlay_name)
    pyautogui.press("enter")
    exit()
