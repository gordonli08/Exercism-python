def primes(limit):
    if limit < 1:
    	return []

    nums = list(range(2,limit+1))
    primes = []
    while nums:
    	prime = nums.pop(0)
    	primes.append(prime)
    	nums = list(filter(lambda y: y % prime, nums))

    return primes

