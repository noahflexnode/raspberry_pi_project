from gpiozero import Device, Button
from gpiozero.pins.mock import MockFactory
import keyboard
import subprocess
from time import sleep

# Set gpiozero pin factory to mock (for testing)
Device.pin_factory = MockFactory()

# Configuration: Set to True to use spacebar, False to use hardware button
USE_SPACEBAR = True

# GPIO pin connected to button (used only if USE_SPACEBAR is False)
button_pin = 18

def toggle_relay():
    try:
        # Call the toggle_relay.py script
        result = subprocess.run(['python3', 'toggle_relay.py'], capture_output=True, text=True)
        # Print the output from toggle_relay.py
        print(result.stdout.strip())
    except Exception as e:
        print(f"An error occurred while toggling the relay: {str(e)}")

# Function to check for spacebar press
def listen_for_spacebar():
    print("Listening for spacebar presses (press 'esc' to exit)...")
    while True:
        try:
            if keyboard.is_pressed('space'):
                toggle_relay()
                sleep(0.3)  # Debounce delay
            if keyboard.is_pressed('esc'):
                print("\nProgram stopped by user")
                break
            sleep(0.1)
        except KeyboardInterrupt:
            print("\nProgram stopped by user")
            break

if USE_SPACEBAR:
    listen_for_spacebar()
else:
    # Code for hardware button (not shown for brevity)
    pass                