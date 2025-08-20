import pyautogui, time
import random
import datetime
from PIL import ImageChops, Image
import pygetwindow as gw

def main():
  
   
    
    while True:
        
                
                    pyautogui.sleep(10)
                    print('#Waiting for 10 seconds before starting the live stream...')
                    # pyautogui.click(x=1818, y=221)
                    # print('#Clicked autoclicker.')
                    # pyautogui.sleep(10)
                    # pyautogui.click(x=818, y=207)
                    # print('#Clicked to start the live stream.')
                    # pyautogui.sleep(15)
                    # print('#15 seconds waited, starting the automation loop.')
                    # print('#started streaming............')
                    # pyautogui.sleep(4)
                    pyautogui.click(x=1818, y=850)
                    pyautogui.sleep(2)
                    print('#started streaming............')

                    
                    timecalculat = random.randint(12 * 60, 16 * 60)
                    minutes = timecalculat // 60
                    seconds = timecalculat % 60
                    print(f"#Next stop in: {minutes} minutes {seconds} seconds")
                    pyautogui.sleep(timecalculat)


                    
                    pyautogui.click(x=1818, y=850)
                    print('#Stopped streaming............')
                  

                    print('#stopped car....')
                    pyautogui.sleep(120)
                    pyautogui.click(x=566, y=866)
                    pyautogui.sleep(30)
                    pyautogui.click(x=240, y=445)
                    t = random.randint(1 * 60, 1 * 60)
                    print('#continue time........')
                    print(f"#Continue for: {t} seconds")
                    pyautogui.sleep(t)
                   
                    
   

if __name__ == "__main__":
    main()