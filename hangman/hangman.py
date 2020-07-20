# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
	def __init__(self, word):
		self.remaining_guesses = 9
		self.status = STATUS_ONGOING
		self.word = word
		self.charLookup = {}
		for k in set(word):
			self.charLookup[k] = '_'

	def guess(self, char):

		if self.status != STATUS_ONGOING:
			raise ValueError('Game is over. No more guesses allowed. Please play again.')

		if char in self.charLookup.keys():
			if self.charLookup[char] == char:
				self.remaining_guesses -= 1
			else:
				self.charLookup[char] = char
		else:
			self.remaining_guesses -= 1

		if all(v!='_' for v in self.charLookup.values()):
			self.status = STATUS_WIN
		if self.remaining_guesses < 0:
			self.status = STATUS_LOSE

	def get_masked_word(self):
		masked = ""
		for c in self.word:
			masked += self.charLookup[c]
		return masked

	def get_status(self):
		return self.status
