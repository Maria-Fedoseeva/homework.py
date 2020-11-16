words = input('Введите слова через пробел: ')
sorted_words = words.split()
for i, word in enumerate(sorted_words, 1):
    print(i, word[:10])

