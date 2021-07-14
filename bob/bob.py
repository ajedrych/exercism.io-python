def response(hey_bob):

    #remove whitespace
    hey_bob = hey_bob.strip()

    if hey_bob.isupper():
        if hey_bob.endswith("?"):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    
    if hey_bob.endswith('?'):
        return "Sure."
    elif hey_bob == "":
        return "Fine. Be that way!"
    else: return "Whatever."
