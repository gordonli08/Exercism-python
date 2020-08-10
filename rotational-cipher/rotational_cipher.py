def rotate(text, key):
    
    return ''.join([convert(letter,key) for letter in text])

def convert(letter, key):
    if not letter.isalpha():
        return letter
    return chr(ord('A') + ((ord(letter) - ord('A') + key) % 26)) if letter.isupper() else chr(ord('a') + ((ord(letter) - ord('a') + key) % 26))

