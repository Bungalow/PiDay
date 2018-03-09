import array
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import UTILS as UTILS
from time import sleep # Import the sleep function from the time module

def zero():
	GPIO.output(A, GPIO.HIGH) # Turn on
	GPIO.output(F, GPIO.HIGH) # Turn on
	GPIO.output(E, GPIO.HIGH) # Turn on
	GPIO.output(D, GPIO.HIGH) # Turn on
	GPIO.output(C, GPIO.HIGH) # Turn on
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.HIGH) # Turn on

A = 16
F = 18
E = 22
D = 32
C = 36
G = 31
B = 33

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(A, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(F, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(E, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(D, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(C, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(G, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(B, GPIO.OUT, initial=GPIO.LOW)

while True:
	zero()