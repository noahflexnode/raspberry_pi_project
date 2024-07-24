import RPi.GPIO as GPIO

def check_relay_status(relay_pin):
    try:
        # Read the state of the relay
        relay_status = GPIO.input(relay_pin)
       
        # Determine and return the status based on the GPIO state
        if relay_status == GPIO.HIGH:
            return "Relay is ON"  # Adjust based on your relay logic (active high or low)
        else:
            return "Relay is OFF"
    except Exception as e:
        # Handle any potential errors during the status check
        return f"Error checking relay status: {str(e)}"

if __name__ == "__main__":
    relayPin = 5  # Ensure this matches the relay pin used in button_detector.py

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(relayPin, GPIO.IN)  # Set relay pin as input to read its status

    print(check_relay_status(relayPin))

    GPIO.cleanup()
