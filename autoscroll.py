import pyautogui
import time

pos = pyautogui.position()
init_pos = [pos.x,pos.y]

while True:
    pos = pyautogui.position()
    #print(pos.x)
    final_pos = [pos.x,pos.y]
    if final_pos[0] == init_pos[0] & final_pos[1] == init_pos[1]:
        pyautogui.scroll(200)
        for i in range(0,1):
            init_pos[i] = final_pos[i]
        print(final_pos)
    time.sleep(1)
    