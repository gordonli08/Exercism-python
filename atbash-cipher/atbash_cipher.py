import string
cipheren = dict(zip(list(string.ascii_lowercase), string.ascii_lowercase[::-1]))
cipherde = dict(zip(string.ascii_lowercase[::-1], list(string.ascii_lowercase)))

def encode(plain_text):
    stripped = [ch for ch in plain_text.lower() if ch.isalnum()]
    stripped = [cipheren[ch] if ch.isalpha() else ch for ch in stripped]
    length = len(stripped)

    return " ".join(["".join(stripped[index:index+5]) for index in range(0,length, 5)])

def decode(ciphered_text):
    ret = ""
    for chunk in ciphered_text.split():
        ret += "".join([cipherde[ch] if ch.isalpha() else ch for ch in chunk])
    return ret
