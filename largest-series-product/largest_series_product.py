import numpy
def largest_product(series, size):
    
    if len(series) < size or size < 0:
        raise ValueError("Please pick a size less than the number of digits in the string and is greater than or equal to 0")
    
    if size == 0:
        return 1
        
    retlist = []
    begin = 0
    end = size
    while end <= len(series):
        retlist.append(numpy.prod(list(map(int, series[begin:end]))))
        begin += 1
        end += 1

    return max(retlist)