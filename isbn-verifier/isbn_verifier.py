def is_valid(isbn):
    values = list(isbn.replace('-',''))

    if len(values) != 10:
    	return False

    for i,v in enumerate(values):
    	if not ((v == 'X' and i == 9) or v.isdigit()):
    		return False
    	if v == 'X':
    		values[i] = 10
    	else:
    		values[i] = int(v)

    if (values[0] * 10 + values[1] * 9 + values[2] * 8 + values[3] * 7 + values[4] * 6 + values[5] * 5 + values[6] * 4 + values[7] * 3 + values[8] * 2 + values[9] * 1) % 11 == 0:
    	return True
    return False


