import pyautogui, time
import random


while True:
    print('started function')
    pyautogui.sleep(4)
  
   

    print('4 sec waited function')
    pyautogui.click(x=1818, y=783)
    pyautogui.sleep(2)
    pyautogui.hotkey("alt", "tab"),
   
#streaming and autiomation started.......

    pyautogui.hotkey("ctrl","1"),
    print('timer started.......')
    timecalculat = random.randint(16* 60,26* 60)
    print(timecalculat)
    pyautogui.sleep(timecalculat)
    pyautogui.hotkey("ctrl","1"),
    print('stoped car....')

#browser ending stream
    pyautogui.click(x=1818, y=783)
    pyautogui.sleep(120)
#dismiss.....
    pyautogui.click(x=612, y=801)
#analysis
    pyautogui.sleep(30)
    pyautogui.click(x=244, y=436)

#switch application

    pyautogui.sleep(5)
    pyautogui.click(x=1619, y=247)
    pyautogui.sleep(5)
    pyautogui.click(x=1635, y=601)
#started stream again




