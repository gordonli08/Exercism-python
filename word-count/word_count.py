from string import punctuation
from collections import Counter

def count_words(sentence):
	frm_sentence = sentence.replace(',',' ').replace('_',' ')

	return Counter([word.strip(punctuation).lower() for word in frm_sentence.split()])

#count_words("\"That's the password: 'PASSWORD 123'!\", cried the Special Agent.\nSo I fled.")