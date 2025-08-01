import pyautogui, time
import random
import datetime

def run_automation():
    """
    # This function contains your original automation logic.
    # It will be called repeatedly during the active hours.
    """
    
    print('#started streaming............')
    pyautogui.sleep(4)
    
    print('#4 sec waited function')
    pyautogui.click(x=1818, y=850) # Ensure these coordinates are correct for your setup
    pyautogui.sleep(2)
    
    # Streaming and automation started.......
    # pyautogui.hotkey("ctrl","1")
    print('#timer started.......')
    timecalculat = random.randint(18 * 60, 22 * 60)
    minutes = timecalculat // 60
    seconds = timecalculat % 60
    print(f"#Next stop in: {minutes} minutes {seconds} seconds")
    pyautogui.sleep(timecalculat)
    # pyautogui.hotkey("ctrl","1") # Assuming this is F8, adjust if needed
    print('#stopped car....')

    # Browser ending stream
    pyautogui.click(x=1818, y=850) # Ensure these coordinates are correct for your setup
    print('#Stopped streaming............')
    pyautogui.sleep(120) # 2 minutes wait
    
    # Dismiss
    pyautogui.click(x=559, y=840) # Ensure these coordinates are correct for your setup
    # Analysis
    pyautogui.sleep(30)
    pyautogui.click(x=245, y=445) # Ensure these coordinates are correct for your setup
    t = random.randint(1 * 60, 1 * 60) # This will always be 60 seconds
    print('#continue time........')
    print(f"#Continue for: {t} seconds")
    pyautogui.sleep(t)

    # Switch application
    pyautogui.sleep(5)
    pyautogui.click(x=1619, y=247) # Ensure these coordinates are correct for your setup
    pyautogui.sleep(5)
    pyautogui.click(x=1635, y=601) # Ensure these coordinates are correct for your setup
    # Started stream again

def main():
    # Define your active time slots
    active_time_slots = [
        (0, 10, 3, 10),      # First slot: 12:10 AM to 3:10 AM
        (5, 20, 23, 15)      # Second slot: 6:20 AM to 11:15 PM
    ]
    
    live_count = 0
    first_live_started = False # নতুন ভেরিয়েবল: এটি নিশ্চিত করবে যে প্রথমবার লাইভ শুরু হয়েছে কিনা

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

                # =========================================================================
                # এই অংশটি শুধুমাত্র একবারই চলবে, যখন প্রথমবার লাইভ শুরু হবে
                print('এই অংশটি শুধুমাত্র একবারই চলবে, যখন প্রথমবার লাইভ শুরু হবে')
                if not first_live_started:
                    pyautogui.sleep(10)
                    print('#Waiting for 10 seconds before starting the live stream...')
                    pyautogui.click(x=1818, y=221)
                    print('#Clicked autoclicker.')
                    pyautogui.sleep(10)
                    pyautogui.click(x=818, y=207) # উদাহরণস্বরূপ কোঅর্ডিনেট, আপনার প্রয়োজন অনুযায়ী পরিবর্তন করুন
                    print('#Clicked to start the live stream.')
                    pyautogui.sleep(15)
                    print('#15 seconds waited, starting the automation loop.')
                    first_live_started = True # একবার রান হয়ে গেলে এটিকে True করে দেওয়া হলো
                    print('#First live started, automation will continue now.')
                # =========================================================================
                
                try:
                    run_automation()
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