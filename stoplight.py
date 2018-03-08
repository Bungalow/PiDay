import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def reset(pins):
	GPIO.output(pins[0], GPIO.LOW) # Turn off
	GPIO.output(pins[1], GPIO.LOW) # Turn off
	GPIO.output(pins[2], GPIO.LOW) # Turn off
	GPIO.output(pins[3], GPIO.LOW) # Turn off
	GPIO.output(pins[4], GPIO.LOW) # Turn off
	GPIO.output(pins[5], GPIO.LOW) # Turn off
	GPIO.output(pins[6], GPIO.LOW) # Turn off
	GPIO.output(pins[7], GPIO.LOW) # Turn off

def stop(pins, yellow):
	if( yellow ):
		yellow(pins, True);
	GPIO.output(pins[0], GPIO.HIGH) # Turn on
	GPIO.output(pins[1], GPIO.HIGH) # Turn on
	GPIO.output(pins[2], GPIO.LOW) # Turn off
	GPIO.output(pins[3], GPIO.LOW) # Turn off
	GPIO.output(pins[4], GPIO.LOW) # Turn off
	GPIO.output(pins[5], GPIO.LOW) # Turn off
	GPIO.output(pins[6], GPIO.LOW) # Turn off
	GPIO.output(pins[7], GPIO.LOW) # Turn off

def yellow(pins, yellowRed ):
	GPIO.output(pins[0], GPIO.LOW) # Turn off
	GPIO.output(pins[1], GPIO.LOW) # Turn off
	GPIO.output(pins[2], GPIO.HIGH) # Turn on
	GPIO.output(pins[3], GPIO.HIGH) # Turn on
	GPIO.output(pins[4], GPIO.LOW) # Turn off
	GPIO.output(pins[5], GPIO.LOW) # Turn off
	GPIO.output(pins[6], GPIO.LOW) # Turn off
	GPIO.output(pins[7], GPIO.LOW) # Turn off
	if yellowRed:
		sleep(5)

def go(pins):
	GPIO.output(pins[0], GPIO.LOW) # Turn off
	GPIO.output(pins[1], GPIO.LOW) # Turn off
	GPIO.output(pins[2], GPIO.LOW) # Turn off
	GPIO.output(pins[3], GPIO.LOW) # Turn on
	GPIO.output(pins[4], GPIO.HIGH) # Turn on
	GPIO.output(pins[5], GPIO.HIGH) # Turn on
	GPIO.output(pins[6], GPIO.LOW) # Turn off
	GPIO.output(pins[7], GPIO.LOW) # Turn off

def cycle(pins)
	reset(pins)
	while True:
		n = raw_input("type q to stop cycle")
		red(pins, False)
		sleep(10)
		green(pins)
		sleep(10)
		red(pins, True)
		sleep(10)
		if n == 'q':
			reset(pins)
			break

pins = [16,18,22,32,36,31,33,37]

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

while True:
	n = raw_input("Please enter 'green', 'yellow', 'red', or 'cycle':")
	if n == 'red':
		print('light changing to yellow then red')
		stop(pins)
	elif n == 'green':
		print('light changin to green')
		go(pins)
	elif n == 'yello':
		print('light changin to yellow')
		yello(pins, False)
	elif 'cycle':
		cycle(pins)
	elif n == 'q' or n == 'exit':
		reset(pins)
		exit()
	else:
		print('invalid command')