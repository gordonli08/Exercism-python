def latest(scores):
	if not scores:
		return 0

	return scores[-1]


def personal_best(scores):

	return max(scores)


def personal_top_three(scores):
	if not scores:
		return 0

	return sorted(scores, reverse=True)[:3]
