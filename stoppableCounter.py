import array
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import UTILS as UTILS
from time import sleep # Import the sleep function from the time module

pins = [16,18,22,32,36,31,33,37]
buttonPin = 11
buttonLEDPin = 13
buttonToggleState = True

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(buttonPin,GPIO.IN)
GPIO.setup(buttonLEDPin, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(buttonLEDPin, GPIO.LOW)

n = 0
while True: # Run forever
	# watch for button press to stop the clock
	pressed = GPIO.input(buttonPin)
	if pressed == GPIO.HIGH:
		buttonToggleState = not buttonToggleState
		sleep(.1)
	if buttonToggleState: 
		GPIO.output(buttonLEDPin, GPIO.HIGH)
	else:
		GPIO.output(buttonLEDPin, GPIO.LOW)
	
	# count up to 255
	if buttonToggleState:
		binaryNumbers = UTILS.int2bin(n)
		values = UTILS.getBinaryOnArray(binaryNumbers)
		for index, ledOn in enumerate(values):
			pin = pins[index];
			if( ledOn ):
				GPIO.output(pin, GPIO.HIGH) # Turn on
			else:
				GPIO.output(pin, GPIO.LOW) # Turn off
		n += 1
		if( n >= 256 ):
			n = 0
	# count by the second
	sleep(1)
GPIO.cleanup()