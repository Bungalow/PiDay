from time import sleep # Import the sleep function from the time module

def int2bin(i):
	bins = list("{0:b}".format(i))
	while( len(bins) != 8 ):
		bins.insert(0,'0')
	return bins

def isOn(val):
	return val == '1'

def getBinaryOnArray(bins):
	valueArray = [];
	for index, bin in enumerate(bins):
		valueArray.insert(index, isOn(bin))
	return valueArray

if __name__ == '__main__':
	UTILS()
