import random
from string import ascii_lowercase


class Cipher:
    def __init__(self, key=None):
        if key is None:
        	self.key = "".join([random.choice(ascii_lowercase) for _ in range(100)])
        else:
        	self.key = key

    def encode(self, text):
        return ''.join([chr(ord('a') + (ord(text[i]) + ord(self.key[i % len(self.key)]) - 2 * ord('a')) % 26) for i in range(len(text))])

    def decode(self, text):
        return ''.join([chr(ord('a') + (ord(text[i]) - ord(self.key[i % len(self.key)])) % 26) for i in range(len(text))])

