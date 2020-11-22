with open('salaries.txt', encoding='utf-8') as doc:
    salaries = []
    lines = doc.readlines()
    for line in lines:
        name, salary = line.split(' - ')
        salaries.append(int(salary))
        if int(salary) < 20000:
            print(line, end='')
    print('\nСредняя зп: ', sum(salaries) / len(salaries))