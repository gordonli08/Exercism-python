def square(number):
	if number < 1 or number > 64:
		raise ValueError('Invalid chessboard square number')
	return 2 ** (number - 1)

def total():
    ret = 0
    for i in range(1,65):
    	ret += square(i)
    return ret
