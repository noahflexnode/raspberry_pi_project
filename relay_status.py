#!/usr/bin/env python3

from gpiozero import Device, OutputDevice
from gpiozero.pins.mock import MockFactory
import sys

Device.pin_factory = MockFactory()
# Define the GPIO pin connected to the relay
RELAY_PIN = 17  # Change this to the actual GPIO pin number you're using

def get_relay_status():
    try:
        # Create an OutputDevice for the relay
        relay = OutputDevice(RELAY_PIN)
        
        # Get the current state of the relay
        state = relay.value
        
        # Close the device to release the GPIO pin
        relay.close()
        
        # Return the state (0 for OFF, 1 for ON)
        return state
    
    except Exception as e:
        # Print error message (optional, for debugging)
        print(f"An error occurred: {str(e)}")
        
        # Return -1 to indicate an error in determining the state
        return -1

if __name__ == "__main__":
    status = get_relay_status()
    if status == 1:
        print("ON")
        sys.exit(0)
    elif status == 0:
        print("OFF")
        sys.exit(0)
    else:
        print("ERROR")
        sys.exit(1)