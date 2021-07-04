def is_pangram(sentence):
    from string import ascii_lowercase
    text = set(sentence.lower())
    alphabet = set(ascii_lowercase)
    if alphabet - text == set([]):
        return True
    return False
    pass
