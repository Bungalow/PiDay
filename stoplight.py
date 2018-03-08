import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def stop():
	yellow();
	GPIO.output(pin[0], GPIO.HIGH) # Turn on
	GPIO.output(pin[1], GPIO.HIGH) # Turn on
	GPIO.output(pin[2], GPIO.LOW) # Turn off
	GPIO.output(pin[3], GPIO.LOW) # Turn off
	GPIO.output(pin[4], GPIO.LOW) # Turn off
	GPIO.output(pin[5], GPIO.LOW) # Turn off
	GPIO.output(pin[6], GPIO.LOW) # Turn off
	GPIO.output(pin[7], GPIO.LOW) # Turn off

def yellow():
	GPIO.output(pin[0], GPIO.LOW) # Turn off
	GPIO.output(pin[1], GPIO.LOW) # Turn off
	GPIO.output(pin[2], GPIO.HIGH) # Turn on
	GPIO.output(pin[3], GPIO.HIGH) # Turn on
	GPIO.output(pin[4], GPIO.LOW) # Turn off
	GPIO.output(pin[5], GPIO.LOW) # Turn off
	GPIO.output(pin[6], GPIO.LOW) # Turn off
	GPIO.output(pin[7], GPIO.LOW) # Turn off
	sleep(5)

def go():
	GPIO.output(pin[0], GPIO.LOW) # Turn off
	GPIO.output(pin[1], GPIO.LOW) # Turn off
	GPIO.output(pin[2], GPIO.LOW) # Turn off
	GPIO.output(pin[3], GPIO.LOW) # Turn on
	GPIO.output(pin[4], GPIO.HIGH) # Turn on
	GPIO.output(pin[5], GPIO.HIGH) # Turn on
	GPIO.output(pin[6], GPIO.LOW) # Turn off
	GPIO.output(pin[7], GPIO.LOW) # Turn off

def walk():
	GPIO.output(pin[0], GPIO.LOW) # Turn off
	GPIO.output(pin[1], GPIO.LOW) # Turn off
	GPIO.output(pin[2], GPIO.LOW) # Turn off
	GPIO.output(pin[3], GPIO.LOW) # Turn on
	GPIO.output(pin[4], GPIO.LOW) # Turn on
	GPIO.output(pin[5], GPIO.LOW) # Turn on
	GPIO.output(pin[6], GPIO.HIGH) # Turn off
	GPIO.output(pin[7], GPIO.HIGH) # Turn off

pins = [16,18,22,32,36,31,33,37]

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

while True:
	n = raw_input("Please enter 'hello':")
	if n == 'stop':
		print('light changing to yellow then red')
		stop()
	elif n == 'go':
		print('light changin to green')
		go()
	elif n == 'walk':
		print('light changin to walk')
		wlak()
	elif n == 'q' or n == 'exit':
		exit()
	else:
		print('invalid command')