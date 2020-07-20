def sum_of_multiples(limit, multiples):
    ret = 0
    for num in range(1,limit):
    	if any([True for mult in multiples if mult != 0 and num%mult == 0]):
    		ret += num
    return ret

