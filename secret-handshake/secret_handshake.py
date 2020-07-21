events = ('wink', 'double blink', 'close your eyes', 'jump')
def commands(number):
    ret = []
    for event in events:
        if number & 1:
            ret.append(event)
        number >>= 1
    return ret[::-1] if number & 1 else ret
