def steps(number):
    if number < 1:
    	raise ValueError('Number must be positive')
    steps = 0
    n = number
    while n != 1:
    	if n % 2 == 0:
    		n = n / 2
    	else:
    		n = 3 * n + 1
    	steps += 1
    return steps