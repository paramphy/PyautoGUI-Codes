import pyautogui
import time 

x = 800
y = 500
while True:
    pyautogui.moveTo(100, 100, duration = 1)
    pyautogui.scroll(200) 
    pyautogui.moveTo(100 + x, 100, duration = 1)
    pyautogui.scroll(200) 
    pyautogui.moveTo(100 + x, 100 + y, duration = 1)
    pyautogui.scroll(200) 
    pyautogui.moveTo(100, 100 + y, duration = 1)
    pyautogui.scroll(200)
    time.sleep(20)  

  

