def color_code(color):
    ret = ''
    for i,v in enumerate(colors()):
    	if v == color:
    		ret = i
    return ret


def colors():
    return [
    	'black',
    	'brown',
    	'red',
    	'orange',
    	'yellow',
    	'green',
    	'blue',
    	'violet',
    	'grey',
    	'white'
    ]
