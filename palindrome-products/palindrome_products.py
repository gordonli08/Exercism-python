def find_palindrome_factors(min_factor, max_factor, smallest=True):
	testrange = (min_factor**2, max_factor**2 + 1) if smallest else (max_factor**2, min_factor**2 - 1, -1)

	for pali in range(*testrange):

		s = str(pali)
		if s == s[::-1] and any(min_factor <= pali // f1 <= max_factor for f1 in range(min_factor, max_factor+1) if pali%f1 == 0):

			return pali, list(((f1,pali//f1) for f1 in range(min_factor, max_factor+1) if pali % f1 == 0 and min_factor <= f1 <= pali//f1 <= max_factor))


def largest(min_factor, max_factor):
	if min_factor > max_factor:
		raise ValueError('Invalid range')
	ret = find_palindrome_factors(min_factor,max_factor,smallest=False)
	if not ret:
		return None, []
	return ret

def smallest(min_factor, max_factor):
	if min_factor > max_factor:
		raise ValueError('Invalid range')
	ret = find_palindrome_factors(min_factor,max_factor)
	if not ret:
		return None, []
	return ret

