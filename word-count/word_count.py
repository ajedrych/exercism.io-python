def count_words(sentence):
    unnecessary = [",", "\t", "\n", "_", ".", ":"]
    cleaned_list = []
    counter = dict()

    for i in unnecessary:
        sentence = sentence.replace(i, " ")

    sentence = sentence.lower().split()

    for word in sentence:
        cleaned_word = ""
        word = word.lstrip("'").rstrip("'")
        for letter in word:
            if letter.isalnum() == True or letter == "'":
                cleaned_word += letter
        cleaned_list.append(cleaned_word)

    for word in cleaned_list:
        if word in counter:
            counter[word] += 1
        else: counter[word] = 1

    return counter
            