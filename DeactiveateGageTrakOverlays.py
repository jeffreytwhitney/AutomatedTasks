import time

import pyautogui
import pywinauto

app = pywinauto.application.Application().connect(title="GAGEtrak 6.8", class_name="OMain")
win = app.window(title="GAGEtrak 6.8", class_name="OMain")

win.SetFocus()
pyautogui.click(900, 276)
time.sleep(4)
pyautogui.click(342, 59)
