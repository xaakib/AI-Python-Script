import pyautogui, time
import random
import datetime

def run_automation():
    """
    This function contains your original automation logic.
    It will be called repeatedly during the active hours.
    """
    print('started streaming............')
    pyautogui.sleep(4)
    
    print('4 sec waited function')
    pyautogui.click(x=1818, y=850) # Ensure these coordinates are correct for your setup
    pyautogui.sleep(2)
    pyautogui.hotkey("alt", "tab")
    
    # Streaming and automation started.......
    pyautogui.hotkey("ctrl","1") # Assuming this is F8, adjust if needed
    print('Sent F8!')
    print('timer started.......')
    timecalculat = random.randint(10 * 60, 12 * 60)
    print(f"Next stop in: {timecalculat} seconds")
    pyautogui.sleep(timecalculat)
    pyautogui.hotkey("ctrl","1") # Assuming this is F8, adjust if needed
    print('stopped car....')

    # Browser ending stream
    pyautogui.click(x=1818, y=850) # Ensure these coordinates are correct for your setup
    print('Stopped streaming............')
    pyautogui.sleep(120) # 2 minutes wait
    
    # Dismiss
    pyautogui.click(x=559, y=821) # Ensure these coordinates are correct for your setup
    # Analysis
    pyautogui.sleep(30)
    pyautogui.click(x=244, y=405) # Ensure these coordinates are correct for your setup
    t = random.randint(1 * 60, 1 * 60) # This will always be 60 seconds
    print('continue time........')
    print(f"Continue for: {t} seconds")
    pyautogui.sleep(t)

    # Switch application
    pyautogui.sleep(5)
    pyautogui.click(x=1619, y=247) # Ensure these coordinates are correct for your setup
    pyautogui.sleep(5)
    pyautogui.click(x=1635, y=601) # Ensure these coordinates are correct for your setup
    # Started stream again

def main():
    start_hour = 1  # 1 AM
    start_minute = 16 # 15 minutes past 1 AM
    end_hour = 9    # 9 AM
    end_minute = 23 # 23 minutes past 9 AM
    
    print("Automation script waiting for active hours...")
    
    while True:
        now = datetime.datetime.now() # Get full datetime object to check hour and minute
        
        # Define the start and end datetime objects for today
        today_start_time = now.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
        today_end_time = now.replace(hour=end_hour, minute=end_minute, second=0, microsecond=0)

        # If the end time has already passed for today, consider the end time to be tomorrow
        # This handles cases like 1 AM to 9 AM, where 1 AM is on one day and 9 AM could be on the next.
        # Given 1:15 AM to 9:23 AM is within the same day, this specific check isn't strictly needed for this range,
        # but it's good practice for ranges that cross midnight.
        if today_end_time < today_start_time: # This condition would be true if end_hour < start_hour
             today_end_time += datetime.timedelta(days=1)
        
        # Check if current time is within the active window (1:15 AM to 9:23 AM)
        if today_start_time <= now < today_end_time:
            print(f"Current time: {now.strftime('%H:%M:%S')} - Running automation.")
            try:
                run_automation()
            except pyautogui.FailSafeException:
                print("PyAutoGUI FailSafe triggered. Mouse moved to a corner. Exiting.")
                break
            except Exception as e:
                print(f"An error occurred: {e}. Continuing after a short delay.")
                time.sleep(60) # Wait a minute before retrying
        else:
            print(f"Current time: {now.strftime('%H:%M:%S')} - Not within active hours ({start_hour}:{start_minute} to {end_hour}:{end_minute}). Waiting...")
            
            # Calculate when the next active period starts
            next_run_time = now.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
            
            # If the next run time for today has already passed, set it for tomorrow
            if next_run_time <= now:
                next_run_time += datetime.timedelta(days=1)
            
            wait_seconds = (next_run_time - now).total_seconds()
            print(f"Waiting for {wait_seconds:.0f} seconds until {next_run_time.strftime('%H:%M:%S')}")
            time.sleep(wait_seconds + 5) # Add a small buffer to ensure we're past the exact minute

if __name__ == "__main__":
    main()