import random
import string

class Robot:
    def __init__(self):
    	self.prevs = set()
    	self.name = ''
    	self.reset()

    def __namegen(self):
    	return ("".join(random.choices(string.ascii_uppercase, k=2)) +
       		"".join(random.choices(string.digits, k=3)))
       	
    def reset(self):
    	if self.name == '':
	    	self.name = self.__namegen()
    	
    	while(self.name in self.prevs):
    		self.name = self.__namegen()

    	self.prevs.add(self.name)
