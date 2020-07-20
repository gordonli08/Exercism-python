import random

class Character:
    def __init__(self):
    	self.strength = self.ability()
    	self.dexterity = self.ability()
    	self.constitution = self.ability()
    	self.intelligence = self.ability()
    	self.wisdom = self.ability()
    	self.charisma = self.ability()
    	self.hitpoints = 10 + modifier(self.constitution)


    def ability(self):
    	return sum(sorted(random.randint(1,6) for _ in range(4))[1:])

def modifier(num):
	return (num - 10) // 2
