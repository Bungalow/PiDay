pins = [16,18,22,32,36,31,33,37]

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)