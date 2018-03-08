import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

def reset(pins):
	GPIO.output(pins[0], GPIO.LOW) # Turn off
	GPIO.output(pins[1], GPIO.LOW) # Turn off
	GPIO.output(pins[2], GPIO.LOW) # Turn off
	GPIO.output(pins[3], GPIO.LOW) # Turn off
	GPIO.output(pins[4], GPIO.LOW) # Turn off
	GPIO.output(pins[5], GPIO.LOW) # Turn off

def red(pins, cycleYellow):
	if cycleYellow:
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
	if yellowRed:
		sleep(5)

def green(pins):
	GPIO.output(pins[0], GPIO.LOW) # Turn off
	GPIO.output(pins[1], GPIO.LOW) # Turn off
	GPIO.output(pins[2], GPIO.LOW) # Turn off
	GPIO.output(pins[3], GPIO.LOW) # Turn on
	GPIO.output(pins[4], GPIO.HIGH) # Turn on
	GPIO.output(pins[5], GPIO.HIGH) # Turn on

def walkCycle(pins, currentCycle):
	if currentCycle%1 == 0:
		walk(pins, True)
	else:
		walk(pins, False)

def walk(pins, walkOn):
	if walkOn:
		GPIO.output(pins[6], GPIO.HIGH) # Turn on
		GPIO.output(pins[7], GPIO.HIGH) # Turn on
	else:
		GPIO.output(pins[6], GPIO.LOW) # Turn off
		GPIO.output(pins[7], GPIO.LOW) # Turn off

def cycle(pins, cycles):
	reset(pins)
	currentCycle = 0
	while currentCycle < cycles:
		print("Starting cycle "+ `currentCycle+1` + ".")
		red(pins, False)
		sleep(10)
		walkCycle(pins,currentCycle)
		green(pins)
		sleep(10)
		red(pins, True)
		sleep(10)
		print("Cycle "+ `currentCycle+1` + "has ended.")
		currentCycle += 1

pins = [16,18,22,32,36,31,33,37]

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

while True:
	n = raw_input("Please enter 'green', 'yellow', 'red', 'redYellow' or 'cycle':")
	if n == 'red':
		print('light changing to red')
		red(pins, False)
	elif n == 'redYellow':
		print('light changing to yellow then red')
		red(pins, True)
	elif n == 'green':
		print('light changin to green')
		green(pins)
	elif n == 'yellow':
		print('light changin to yellow')
		yellow(pins, False)
	elif 'cycle':
		print('running cycle twice')
		input = int(input("How many times?"))
		cycle(pins, input)
	elif n == 'q' or n == 'exit':
		reset(pins)
		exit()
	else:
		print('invalid command')