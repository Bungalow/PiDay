import array
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import UTILS as UTILS
from time import sleep # Import the sleep function from the time module

pins = [16,18,22,32,36,31,33,37]

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

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
	n += 1
	if( n >= 256 ):
		n = 0
	sleep(1)

GPIO.cleanup()