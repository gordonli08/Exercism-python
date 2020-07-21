def abbreviate(words):
    frm_words = words.replace(',',' ').replace('_',' ').replace('-',' ')
    return ''.join([word.strip()[0].upper() for word in frm_words.split()])
