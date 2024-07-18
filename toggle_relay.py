from gpiozero import Device, OutputDevice
from gpiozero.pins.mock import MockFactory
import sys
import os

Device.pin_factory = MockFactory()

RELAY_PIN = 17  # Change this to the actual GPIO pin number you're using
STATE_FILE = '/home/pi/scripts/relay_state.txt'  # File to store the relay state

def ensure_directory_exists(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def read_relay_state():
    ensure_directory_exists(STATE_FILE)
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            state = f.read().strip()
            return state == 'ON'
    else:
        with open(STATE_FILE, 'w') as f:
            f.write('OFF')
        return False  # Default state is OFF if file doesn't exist

def write_relay_state(state):
    with open(STATE_FILE, 'w') as f:
        f.write('ON' if state else 'OFF')

def toggle_relay():
    try:
        # Read the current state from the file
        current_state = read_relay_state()
        
        # Create an OutputDevice for the relay
        relay = OutputDevice(RELAY_PIN)
        
        # Toggle the relay state
        if current_state:
            relay.off()
        else:
            relay.on()
        
        # Save the new state to the file
        new_state = not current_state
        write_relay_state(new_state)
        
        
        print(f"Relay state toggled. New state: {'ON' if new_state else 'OFF'}")
        
        # Close the device to release the GPIO pin
        relay.close()
        
        # Return 0 to indicate success
        return 0
    
    except Exception as e:
        
        print(f"An error occurred: {str(e)}")
        
        # Return 1 to indicate failure
        return 1

if __name__ == "__main__":
    # Run the toggle_relay function and use its return value as the script's exit code
    sys.exit(toggle_relay())
