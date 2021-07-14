def is_isogram(string):
    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace("-", "")
    
    string_set = set(string)

    if len(list(string)) == len(list(string_set)):
        return True
    else: return False

    