def score(word):
    points = {'AEIOULNRST' : 1,
        'DG' : 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10}

    word = word.upper()
    counter = 0

    for letter in word:
        for i in points.keys():
            for j in i:
                if j == letter:
                    counter += points.get(i)
    return counter
