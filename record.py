import pyautogui, time
import random
import datetime

def run_automation():
    """
    # This function contains your original automation logic.
    # It will be called repeatedly during the active hours.
    """
    
    print('#started Recording............')
    pyautogui.sleep(4)
    
    print('#4 sec waited function')
    pyautogui.click(x=1809, y=880) # Ensure these coordinates are correct for your setup
    pyautogui.sleep(2)
    
    # Streaming and automation started.......
    pyautogui.hotkey("ctrl","1")
    print('#timer started.......')
    timecalculat = random.randint(1 * 60, 3 * 60)
    minutes = timecalculat // 60
    seconds = timecalculat % 60
    print(f"#Next stop in: {minutes} minutes {seconds} seconds")
    pyautogui.sleep(timecalculat)
    pyautogui.hotkey("ctrl","1") # Assuming this is F8, adjust if needed
    print('#stopped car....')

    # Browser ending stream
    pyautogui.click(x=1809, y=880) # Ensure these coordinates are correct for your setup
    print('#Stopped Recording............')
    pyautogui.sleep(5)

    # Started stream again

def main():


    print("#Automation script waiting for active hours...")
    
    while True:
       
                    run_automation()
                   

if __name__ == "__main__":
    main()