import pyautogui
import time 

def ghost():
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
        #return("It is Gosting") 

#def send_mail():
#posfile = open('pos.txt','w')
#x = []
#y = []
#while True:
#    pos = pyautogui.position()
#    posfile.write(str(pos[0]))
#    posfile.write(",")
#    posfile.write(str(pos[1]))
#    posfile.write("\n")
#    time.sleep(1)
with open("pos.txt", "r") as file: 
    word = []
    data = file.readlines() 
    for line in data: 
        word.append(line.rstrip('\n').split(',')) 
    print(word) 
for x,y in word:
    print(x,y)
    pyautogui.moveTo(int(x), int(y), duration = 1)
    time.sleep(.1)
