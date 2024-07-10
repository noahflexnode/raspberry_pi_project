from gpiozero import Device, OutputDevice
from gpiozero.pins.mock import MockFactory
import sys

Device.pin_factory = MockFactory()

RELAY_PIN = 17  # Change this to the actual GPIO pin number you're using

def toggle_relay():
    try:
        # Create an OutputDevice for the relay
        relay = OutputDevice(RELAY_PIN)
        
        # Toggle the relay state
        relay.toggle()
        
        # Print the new state (optional, for debugging)
        print(f"Relay state toggled. New state: {'ON' if relay.value == 1 else 'OFF'}")
        
        # Close the device to release the GPIO pin
        relay.close()
        
        # Return 0 to indicate success
        return 0
    
    except Exception as e:
        # Print error message (optional, for debugging)
        print(f"An error occurred: {str(e)}")
        
        # Return 1 to indicate failure
        return 1

if __name__ == "__main__":
    # Run the toggle_relay function and use its return value as the script's exit code
    sys.exit(toggle_relay())