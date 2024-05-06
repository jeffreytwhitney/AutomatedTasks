import os
import time

import pyautogui

os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\GAGEtrak 6.8\\GAGEtrak 6.8.lnk")
time.sleep(4)
pyautogui.typewrite("Shop")
pyautogui.typewrite("\t")
pyautogui.typewrite("1234")
pyautogui.press('enter')
