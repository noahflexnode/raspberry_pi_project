#!/usr/bin/env python3

import sys
import os
#to do change stateless
STATE_FILE = '/home/pi/scripts/relay_state.txt'  # File to store the relay state

def read_relay_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as f:
            state = f.read().strip()
            if state == 'ON':
                return 1
            elif state == 'OFF':
                return 0
    return -1  # Return -1 if the state could not be determined

def get_relay_status():
    try:
        # Read the current state from the file
        return read_relay_state()
    
    except Exception as e:
        
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
