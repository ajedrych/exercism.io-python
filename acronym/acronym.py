def abbreviate(words):
    words = words.replace("-", " ").replace("_", " ").upper().split()
    acronym = ""
    for part in words:
        acronym += str(part[0])
    return acronym