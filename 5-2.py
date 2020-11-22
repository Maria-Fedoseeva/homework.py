with open('text.txt', encoding='utf-8') as text:
    lines = text.readlines()
print('Количество строк: ', len(lines))
for num_line, line in enumerate(lines, start=1):
    print('{} строка содержит {} слов'.format(num_line, len(line.split())))