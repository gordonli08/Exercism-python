def is_paired(input_string):
    
    opening = '({['
    closing = ')}]'
    brackets = dict(zip(opening,closing))
    stack = []

    for char in input_string:
    	if char in opening:
    		stack.append(brackets[char])
    	elif char in closing:
    		if not stack or char != stack.pop():
    			return False

    return not stack


