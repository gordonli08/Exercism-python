def triplets_with_sum(number):
	triplets = []
	for a in range(1, number // 3 + 1):
		for b in range(a+1, number // 2 + 1):
			c = number - a - b
			if is_triplet([a, b, c]):
				triplets.append([a, b, c])
	return triplets



def triplets_in_range(start, end):
    pass


def is_triplet(triplet):
    a, b, c = triplet
    return a < b < c and a ** 2 + b ** 2 == c ** 2
