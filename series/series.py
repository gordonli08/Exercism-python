def slices(series, length):
    if len(series) < length or length < 1:
    	raise ValueError("Please pick a length less than the number of digits in the string and is greater than 1")


    retlist = []
    begin = 0
    end = length
    while end <= len(series):
    	retlist.append(series[begin:end])
    	begin += 1
    	end += 1

    return retlist
