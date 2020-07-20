def equilateral(sides):
    if all(side != 0 for side in sides) and len(set(sides)) <= 1:
    	return True
    return False


def isosceles(sides):
    if istriangle(sides) and len(set(sides)) <= 2:
    	return True
    return False


def scalene(sides):
	if istriangle(sides) and len(set(sides)) == 3:
		return True
	return False

def istriangle(sides):
	sortsides = sorted(sides)
	if all(side != 0 for side in sides) and sortsides[0]+sortsides[1]>sortsides[2]:
		return True
	return False