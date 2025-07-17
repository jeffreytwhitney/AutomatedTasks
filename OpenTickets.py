import webbrowser
import pyautogui
import time

webbrowser.open('http://10.146.2.11:8080/ehelpdesk/login.glml')
time.sleep(1)
pyautogui.typewrite("jtwhitney")
pyautogui.typewrite("\t")
pyautogui.typewrite("An0nym0usly!")
pyautogui.press('enter')