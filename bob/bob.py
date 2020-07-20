def response(hey_bob):
    phrase = hey_bob.strip()
    if phrase == '':
    	return "Fine. Be that way!"
    elif phrase[-1] == '?' and phrase.isupper():
    	return "Calm down, I know what I'm doing!"
    elif phrase.isupper():
    	return "Whoa, chill out!"
    elif phrase[-1] == '?':
    	return "Sure."
    return "Whatever."
