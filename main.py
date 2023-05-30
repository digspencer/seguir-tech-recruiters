import pyautogui
import time

conectar = pyautogui.locateOnScreen('conectar.png')

while not conectar:
    time.sleep(1)
    pyautogui.scroll(-20)