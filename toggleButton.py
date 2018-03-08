import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.OUT, initial=GPIO.LOW)

ledOn = False

while True:
	print(GPIO.input(11))
	pressed = PGIO.input(11)
	if pressed:
		ledOn = not ledOn

	if ledOn: 
		GPIO.output(13, GPIO.HIGH)
	else:
		GPIO.output(13, GPIO.LOW)
