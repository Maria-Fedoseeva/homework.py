with open('text.txt', 'w', encoding='utf-8') as text:
    while True:
        line = input('Введите текст: ')
        if line == '':
            break
        text.write(line + '\n')