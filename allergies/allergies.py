aller_items = [
	'eggs',
	'peanuts',
	'shellfish',
	'strawberries',
	'tomatoes',
	'chocolate',
	'pollen',
	'cats'
]

class Allergies:

    def __init__(self, score):
        self.score = score


    def allergic_to(self, item):
        return self.score >> aller_items.index(item) & 1 == 1

    @property
    def lst(self):
        return [aller for aller in aller_items if self.allergic_to(aller)]

