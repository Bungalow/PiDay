import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def stop(pins):
	yellow(pins);
	GPIO.output(pins[0], GPIO.HIGH) # Turn on
	GPIO.output(pins[1], GPIO.HIGH) # Turn on
	GPIO.output(pins[2], GPIO.LOW) # Turn off
	GPIO.output(pins[3], GPIO.LOW) # Turn off
	GPIO.output(pins[4], GPIO.LOW) # Turn off
	GPIO.output(pins[5], GPIO.LOW) # Turn off
	GPIO.output(pins[6], GPIO.LOW) # Turn off
	GPIO.output(pins[7], GPIO.LOW) # Turn off

def yellow(pins):
	GPIO.output(pins[0], GPIO.LOW) # Turn off
	GPIO.output(pins[1], GPIO.LOW) # Turn off
	GPIO.output(pins[2], GPIO.HIGH) # Turn on
	GPIO.output(pins[3], GPIO.HIGH) # Turn on
	GPIO.output(pins[4], GPIO.LOW) # Turn off
	GPIO.output(pins[5], GPIO.LOW) # Turn off
	GPIO.output(pins[6], GPIO.LOW) # Turn off
	GPIO.output(pins[7], GPIO.LOW) # Turn off
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

def walk(pins):
	GPIO.output(pins[0], GPIO.LOW) # Turn off
	GPIO.output(pins[1], GPIO.LOW) # Turn off
	GPIO.output(pins[2], GPIO.LOW) # Turn off
	GPIO.output(pins[3], GPIO.LOW) # Turn on
	GPIO.output(pins[4], GPIO.LOW) # Turn on
	GPIO.output(pins[5], GPIO.LOW) # Turn on
	GPIO.output(pins[6], GPIO.HIGH) # Turn off
	GPIO.output(pins[7], GPIO.HIGH) # Turn off

pins = [16,18,22,32,36,31,33,37]

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

while True:
	n = raw_input("Please enter 'hello':")
	if n == 'stop':
		print('light changing to yellow then red')
		stop(pins)
	elif n == 'go':
		print('light changin to green')
		go(pins)
	elif n == 'walk':
		print('light changin to walk')
		wlak(pins)
	elif n == 'q' or n == 'exit':
		exit()
	else:
		print('invalid command')