def find_anagrams(word, candidates):
    expected = []

    for words in candidates:
        if word.lower() != words.lower():
            if sorted(word.lower()) == sorted(words.lower()):
                expected.append(words)

    return expected
