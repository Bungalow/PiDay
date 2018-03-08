import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.OUT)

ledOn = False

while True:
	if GPIO.input(11) == False:
		ledOn = !ledOn
	if ledOn: 
		GPIO.output(13,GPIO.HIGH)
	else : 
		GPIO.output(13,GPIO.LOW)
