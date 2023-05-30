import pyautogui
import time

conectar = pyautogui.locateOnScreen('conectar.png')

while not conectar:
    pyautogui.scroll(-20)