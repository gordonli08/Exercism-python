def is_armstrong_number(number):
    aNumber = 0
    numlist = [int(d) for d in str(number)]
    for digit in numlist:
    	aNumber += digit ** len(numlist)

    return number == aNumber

