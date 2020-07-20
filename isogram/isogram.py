def is_isogram(string):
    if string == "":
    	return True
    else:
    	string = string.lower()
    	for letter in string:
    		if string.count(letter) > 1 and letter.isalpha():
    			return False
    return True