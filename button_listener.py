from time import sleep
import RPi.GPIO as GPIO
from toggle_relay import toggle_relay

delay = 0.2
inPin = 3

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

buttonState = 1
buttonStateOld = 1
printState = False

try:
	while True:
		buttonState = GPIO.input(inPin)
		if buttonState == 1 and buttonStateOld == 0:
			printState = toggle_relay(printState)
			buttonStateOld = buttonState
			sleep(delay)
		else:
			buttonStateOld = buttonState

except KeyboardInterrupt:
	GPIO.cleanup()
	print("GPIO cleaned")
