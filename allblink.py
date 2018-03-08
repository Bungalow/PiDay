import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

pins = {16,18,22,32,36,31,33,37}

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

while True: # Run forever
	for pin in pins:
		GPIO.output(pin, GPIO.HIGH) # Turn on

	sleep(1) # Sleep for 1 second

	for pin in pins:
		GPIO.output(pin, GPIO.LOW) # Turn off

	sleep(1) # Sleep for 1 second

GPIO.cleanup()
