import pyautogui, time
import random
import datetime
from PIL import ImageChops, Image
import pygetwindow as gw

def main():
    active_time_slots = [
        (8, 10, 23, 15),
        (0, 20, 9, 10)
    ]
    
    live_count = 0

    print("#Automation script waiting for active hours...")
    
    while True:
        now = datetime.datetime.now()
        is_active_hour = False
        
        for start_hour, start_minute, end_hour, end_minute in active_time_slots:
            today_start_time = now.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
            today_end_time = now.replace(hour=end_hour, minute=end_minute, second=0, microsecond=0)

            if today_end_time < today_start_time:
                today_end_time += datetime.timedelta(days=1)
            
            if today_start_time <= now < today_end_time:
                is_active_hour = True
                print(f"#Current time: {now.strftime('%H:%M:%S')} - Running automation within {start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}.")

                try:
                    try:
                        emulator_window = gw.getWindowsWithTitle('BlueStacks App Player')[0]
                        current_region = (emulator_window.left, emulator_window.top, emulator_window.width, emulator_window.height)
                    except IndexError:
                        print("Emulator window not found. Please ensure it's open.")
                        time.sleep(60)
                        continue

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
                    pyautogui.hotkey("ctrl","1")

                    
                    timecalculat = random.randint(16 * 60, 22 * 60)
                    minutes = timecalculat // 60
                    seconds = timecalculat % 60
                    print(f"#Next stop in: {minutes} minutes {seconds} seconds")


                    

                    is_hung = False
                    start_time = time.time()
                    last_three_screenshots = []  # শেষ তিনটি স্ক্রিনশট সংরক্ষণের জন্য
                    check_interval = 30  # প্রতি 30 সেকেন্ডে একবার চেক করা হবে

                    while time.time() - start_time < timecalculat:
                        time_to_wait = check_interval
                        if time.time() - start_time + time_to_wait > timecalculat:
                            time_to_wait = timecalculat - (time.time() - start_time)
                        
                        if time_to_wait > 0:
                            pyautogui.sleep(time_to_wait)
                        
                        print("Checking for hang... [Every 30-second check]")
                        new_screenshot = pyautogui.screenshot(region=current_region).convert('RGB')
                        
                        last_three_screenshots.append(new_screenshot)
                        if len(last_three_screenshots) > 3:
                            last_three_screenshots.pop(0)  # চতুর্থ স্ক্রিনশট যোগ হলে, প্রথমটি মুছে ফেলা হবে
                            
                        if len(last_three_screenshots) == 3:
                            diff1 = ImageChops.difference(last_three_screenshots[0], last_three_screenshots[1]).getbbox()
                            diff2 = ImageChops.difference(last_three_screenshots[1], last_three_screenshots[2]).getbbox()
                            
                            if diff1 is None and diff2 is None:
                                print('Game has likely hung (3 consecutive static screenshots). Stopping live stream.')
                                
                                pyautogui.click(x=1047, y=872) # stop automatically game
                                # # call anyone direct sim 
                                # is_hung = True
                                # break
                            else:
                                print("Game is running, continuing stream...")




                    pyautogui.hotkey("ctrl","1")
                    pyautogui.click(x=1818, y=850)
                    print('#Stopped streaming............')
                    
                    if is_hung:
                        # একবার হ্যাং হলে স্ক্রিপ্ট পুরোপুরি বন্ধ হয়ে যাবে
                        print("#Hang detected. Exiting script.")
                        return 

                    print('#stopped car....')
                    last_three_screenshots.clear()  # স্ক্রিনশট ক্লিয়ার করা হচ্ছে পরবর্তী চেকের জন্য
                    pyautogui.sleep(120)
                    pyautogui.click(x=566, y=866)
                    pyautogui.sleep(30)
                    pyautogui.click(x=240, y=445)
                    t = random.randint(1 * 60, 1 * 60)
                    print('#continue time........')
                    print(f"#Continue for: {t} seconds")
                    pyautogui.sleep(t)
                   
                    
                    live_count += 1
                    print(f"#Total successful live runs: {live_count}")

                except pyautogui.FailSafeException:
                    print("#PyAutoGUI FailSafe triggered. Mouse moved to a corner. Exiting.")
                    return
                except Exception as e:
                    print(f"#An error occurred: {e}. Continuing after a short delay.")
                    time.sleep(60)
                break
        
        if not is_active_hour:
            print(f"#Current time: {now.strftime('%H:%M:%S')} - Not within any active hours. Waiting...")
            
            next_run_time = None
            for start_hour, start_minute, _, _ in active_time_slots:
                potential_next_run = now.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
                if potential_next_run <= now:
                    potential_next_run += datetime.timedelta(days=1)
                
                if next_run_time is None or potential_next_run < next_run_time:
                    next_run_time = potential_next_run
            
            if next_run_time:
                wait_seconds = (next_run_time - now).total_seconds()
                print(f"#Waiting for {wait_seconds:.0f} seconds until {next_run_time.strftime('%H:%M:%S')}")
                time.sleep(wait_seconds + 5)

if __name__ == "__main__":
    main()