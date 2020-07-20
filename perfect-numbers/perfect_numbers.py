import math

def classify(number):

	if number < 1:
		raise ValueError("Not a natural number")

	maxfactor = math.floor(math.sqrt(number))
	aliquot = 0
	for i in range(1,maxfactor + 1):
		if number % i == 0:
			if i * i == number:
				aliquot += i
			else:
				aliquot += i + (number/i)

	aliquot -= number

	if aliquot > number:
		return "abundant"
	if aliquot < number:
		return "deficient"

	return "perfect"