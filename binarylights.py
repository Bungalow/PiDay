import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import UTILS as UTILS
from time import sleep # Import the sleep function from the time module

def int2bin(i):
	return list("{0:b}".format(i))

def isOn(val):
	return val == '1'


pins = {16,18,22,32,36,31,33,37}

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

n = 0
while True: # Run forever
	binaryNumbers = UTILS.int2bin(n)
	for index, pin in pins:
		if UTILS.isOn(index):
			GPIO.output(pin, GPIO.HIGH) # Turn on
		else:
			GPIO.output(pin, GPIO.LOW) # Turn on
	n += 1
	sleep(1) # Sleep for 1 second