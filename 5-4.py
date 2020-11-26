with open('eng.txt', encoding='utf-8') as numbers:
    lines = numbers.readlines()

with open('rus.txt', 'w', encoding='utf-8') as numbers:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        numbers.write(line)