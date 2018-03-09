import array
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import UTILS as UTILS
from time import sleep # Import the sleep function from the time module

def zero():
	GPIO.output(A, GPIO.LOW) # Turn on
	GPIO.output(F, GPIO.LOW) # Turn on
	GPIO.output(E, GPIO.LOW) # Turn on
	GPIO.output(D, GPIO.LOW) # Turn on
	GPIO.output(C, GPIO.LOW) # Turn on
	GPIO.output(G, GPIO.HIGH) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn on

A = 16
F = 18
E = 22
D = 32
C = 36
G = 31
B = 33

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

GPIO.setup(A, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(F, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(E, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(D, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(C, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(G, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(B, GPIO.OUT, initial=GPIO.HIGH)

while True:
	zero()