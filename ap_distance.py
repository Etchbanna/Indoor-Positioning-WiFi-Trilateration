import math


def ap_distance(signal_power,frequency):
	exp = (27.55 - (20 * math.log10(freq)) +abs(power)) / 20.0
	distance=pow(10.0,exp)
	return distance
	
	

