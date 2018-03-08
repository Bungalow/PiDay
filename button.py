import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(17,GPIO.IN)
GPIO.setup(27,GPIO.OUT)

while True:
	if GPIO.input(17) == False:
		GPIO.output(27,GPIO.HIGH)
	elif GPIO.input(17) == True:
		GPIO.output(27,GPIO.LOW)