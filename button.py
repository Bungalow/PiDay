import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(11,GPIO.IN)
GPIO.setup(13,GPIO.OUT)

while True:
	if GPIO.input(11) == False:
		GPIO.output(13,GPIO.HIGH)
	elif GPIO.input(11) == True:
		GPIO.output(13,GPIO.LOW)