def int2bin(i):
	return list("{0:b}".format(i))

def isOn(val):
	return val == '1'

for i in range(256):
	binaryNumbers = int2bin(i)
	print(binaryNumbers)
	for binaryDigit in binaryNumbers:
		print(isOn(binaryDigit))
