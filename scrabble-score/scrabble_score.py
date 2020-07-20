points = dict(
    [(letter,1) for letter in 'AEIOULNRST'] +
    [(letter,2) for letter in 'DG'] +
    [(letter,3) for letter in 'BCMP'] +
    [(letter,4) for letter in 'FHVWY'] +
    [('K',5)] +
    [(letter,8) for letter in 'JX'] +
    [(letter,10) for letter in 'QZ']
)

def score(word):
    if not word.isalpha():
    	return 0

    return sum([points[letter] for letter in word.upper()])
