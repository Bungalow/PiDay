import array
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import UTILS as UTILS
from time import sleep # Import the sleep function from the time module

pins = [16,18,22,32,36,31,33,37]
buttonPin = 11
buttonLEDPin = 13
direction = "UP"
buttonToggleState = True

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11,GPIO.IN)
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(13, GPIO.LOW)


n = 0
while True: # Run forever
	binaryNumbers = UTILS.int2bin(n)
	values = UTILS.getBinaryOnArray(binaryNumbers)
	for index, ledOn in enumerate(values):
		pin = pins[index];
		if( ledOn ):
			GPIO.output(pin, GPIO.HIGH) # Turn on
		else:
			GPIO.output(pin, GPIO.LOW) # Turn off

	pressed = GPIO.input(11)
	if pressed == GPIO.HIGH:
		buttonToggleState = not buttonToggleState
		sleep(.1)
	if state: 
		GPIO.output(13, GPIO.HIGH)
		direction == "UP"
	else:
		GPIO.output(13, GPIO.LOW)
		direction == "DOWN"

	if direction == "UP":
		n += 1
		if( n >= 256 ):
			n = 0
	elif direction == "DOWN":
		n -= 1
		if( n < 0 ):
			n = 255
	sleep(1)

GPIO.cleanup()