import subprocess
from pynput import keyboard, mouse

# Replace 'localhost:5555' with your specific emulator device ID, if needed
EMULATOR_DEVICE_ID = "localhost:5555"

# Define key mappings for keyboard controls (simulated D-pad for car movement)
key_mapping = {
    keyboard.Key.up: f"adb -s {EMULATOR_DEVICE_ID} shell input keyevent 19",    # D-Pad Up (Move Forward)
    keyboard.Key.down: f"adb -s {EMULATOR_DEVICE_ID} shell input keyevent 20",  # D-Pad Down (Move Backward)
    keyboard.Key.left: f"adb -s {EMULATOR_DEVICE_ID} shell input keyevent 21",  # D-Pad Left (Turn Left)
    keyboard.Key.right: f"adb -s {EMULATOR_DEVICE_ID} shell input keyevent 22", # D-Pad Right (Turn Right)
    keyboard.Key.enter: f"adb -s {EMULATOR_DEVICE_ID} shell input keyevent 66", # Enter (Action/Confirm)
    keyboard.Key.esc: f"adb -s {EMULATOR_DEVICE_ID} shell input keyevent 4",    # Back (Exit Menu)
}

# Function to send ADB commands
def send_adb_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Handle keyboard inputs
def on_keyboard_press(key):
    if key in key_mapping:
        adb_command = key_mapping[key]
        send_adb_command(adb_command)

# Handle mouse clicks (to simulate screen taps)
def on_mouse_click(x, y, button, pressed):
    if pressed:
        adb_command = f"adb -s {EMULATOR_DEVICE_ID} shell input tap {x} {y}"
        send_adb_command(adb_command)
        print(f"Mouse clicked at ({x}, {y}) on emulator")

# Start listening for keyboard and mouse events
def start_listening():
    print("Listening for keyboard and mouse inputs...")
    
    # Start keyboard listener
    keyboard_listener = keyboard.Listener(on_press=on_keyboard_press)
    keyboard_listener.start()

    # Start mouse listener
    mouse_listener = mouse.Listener(on_click=on_mouse_click)
    mouse_listener.start()

    # Keep the script running to listen for inputs
    keyboard_listener.join()
    mouse_listener.join()

if __name__ == "__main__":
    start_listening()
