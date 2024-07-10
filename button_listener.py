from gpiozero import Device, DigitalOutputDevice, Button
from gpiozero.pins.mock import MockFactory
import keyboard
from time import sleep

# Set gpiozero pin factory to mock (for testing)
Device.pin_factory = MockFactory()

# Configuration: Set to True to use spacebar, False to use hardware button
USE_SPACEBAR = True

# GPIO pin connected to relay
relay_pin = 17  # Replace with your actual GPIO pin number

# GPIO pin connected to button (used only if USE_SPACEBAR is False)
button_pin = 18  

relay = DigitalOutputDevice(relay_pin)


def toggle_relay():
    relay.toggle()
    if relay.is_active:
        print("Lights are ON")
    else:
        print("Lights are OFF")

# Function to check for spacebar press
def listen_for_spacebar():
    print("Listening for spacebar presses (press 'esc' to exit)...")
    while True:
        try:
            if keyboard.is_pressed('space'):  
                toggle_relay()
                sleep(0.3)  
            if keyboard.is_pressed('esc'):
                print("\nProgram stopped by user")
                break
            sleep(0.1) 
        except KeyboardInterrupt:
            print("\nProgram stopped by user")
            break

# Function to check for hardware button press
def listen_for_button():
    button = Button(button_pin, pull_up=True)  
    
    button.when_pressed = toggle_relay

    print("Listening for hardware button presses (press 'esc' to exit)...")
    try:
        while True:
            sleep(1)  
    except KeyboardInterrupt:
        print("\nProgram stopped by user")


if USE_SPACEBAR:
    listen_for_spacebar()
else:
    listen_for_button()
 