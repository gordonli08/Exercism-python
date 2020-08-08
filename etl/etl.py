from collections import defaultdict

def transform(legacy_data):
    ret = {}
    for score, letters in legacy_data.items():
        for letter in letters:
            ret[letter.lower()] = score
    return ret
