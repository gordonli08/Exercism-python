def find_anagrams(word, candidates):
    
    origword = sorted(word.lower())

    ret = []
    for c in candidates:
    	csorted = sorted(c.lower())
    	if origword == csorted and word.lower() != c.lower():
    		ret.append(c)

    return ret
