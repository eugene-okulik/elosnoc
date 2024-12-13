def words_multiplier(dict_words):
    for key, value in dict_words.items():
        print(key * int(value))


words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
words_multiplier(words)
