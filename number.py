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

def one():
	GPIO.output(A, GPIO.LOW) # Turn off
	GPIO.output(F, GPIO.HIGH) # Turn on
	GPIO.output(E, GPIO.HIGH) # Turn on
	GPIO.output(D, GPIO.LOW) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn on

def two():
	GPIO.output(A, GPIO.HIGH) # Turn off
	GPIO.output(F, GPIO.LOW) # Turn off
	GPIO.output(E, GPIO.HIGH) # Turn off
	GPIO.output(D, GPIO.HIGH) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.HIGH) # Turn off
	GPIO.output(B, GPIO.HIGH) # Turn off

def three():
	GPIO.output(A, GPIO.LOW) # Turn off
	GPIO.output(F, GPIO.LOW) # Turn off
	GPIO.output(E, GPIO.LOW) # Turn off
	GPIO.output(D, GPIO.LOW) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn off

def four():
	GPIO.output(A, GPIO.LOW) # Turn off
	GPIO.output(F, GPIO.LOW) # Turn off
	GPIO.output(E, GPIO.LOW) # Turn off
	GPIO.output(D, GPIO.LOW) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn off

def five():
	GPIO.output(A, GPIO.LOW) # Turn off
	GPIO.output(F, GPIO.LOW) # Turn off
	GPIO.output(E, GPIO.LOW) # Turn off
	GPIO.output(D, GPIO.LOW) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn off

def six():
	GPIO.output(A, GPIO.LOW) # Turn off
	GPIO.output(F, GPIO.LOW) # Turn off
	GPIO.output(E, GPIO.LOW) # Turn off
	GPIO.output(D, GPIO.LOW) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn off

def seven():
	GPIO.output(A, GPIO.LOW) # Turn off
	GPIO.output(F, GPIO.LOW) # Turn off
	GPIO.output(E, GPIO.LOW) # Turn off
	GPIO.output(D, GPIO.LOW) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn off

def eight():
	GPIO.output(A, GPIO.LOW) # Turn off
	GPIO.output(F, GPIO.LOW) # Turn off
	GPIO.output(E, GPIO.LOW) # Turn off
	GPIO.output(D, GPIO.LOW) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn off

def nine():
	GPIO.output(A, GPIO.LOW) # Turn off
	GPIO.output(F, GPIO.LOW) # Turn off
	GPIO.output(E, GPIO.LOW) # Turn off
	GPIO.output(D, GPIO.LOW) # Turn off
	GPIO.output(C, GPIO.LOW) # Turn off
	GPIO.output(G, GPIO.LOW) # Turn off
	GPIO.output(B, GPIO.LOW) # Turn off

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
	sleep(1)
	one()
	sleep(1)