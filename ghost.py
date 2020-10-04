import pyautogui
import time 

def ghost():
    x = 800
    y = 500

    pyautogui.moveTo(100, 100, duration = 1)
    pyautogui.scroll(200) 
    pyautogui.moveTo(100 + x, 100, duration = 1)
    pyautogui.scroll(200) 
    pyautogui.moveTo(100 + x, 100 + y, duration = 1)
    pyautogui.scroll(200) 
    pyautogui.moveTo(100, 100 + y, duration = 1)
    pyautogui.scroll(200)
    print("#")
    
while True:
    ghost()
    time.sleep(20)