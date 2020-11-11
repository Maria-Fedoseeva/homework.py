month = int(input('Введите номер месяца: '))

if month <= 0 or month >= 13:
    print('Введенно некорректное число')

elif month >= 3 and month <= 5:
    print('Весна')

elif month >= 6 and month <= 8:
    print('Лето')

elif month >= 9 and month <= 11:
    print('Осень')

else:
    print('Зима')


seasons_dict = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима'
}
month = int(input('Введите номер месяца: '))

if month <= 0 or month >= 13:
    print('Введенно некорректное число')
else:
    print(seasons_dict[month])


seasons_list = ['',
                'Зима',
                'Зима',
                'Весна',
                'Весна',
                'Весна',
                'Лето',
                'Лето',
                'Лето',
                'Осень',
                'Осень',
                'Осень',
                'Зима']
month = int(input('Введите номер месяца: '))

if month <= 0 or month >= 13:
    print('Введенно некорректное число')
else:
    print(seasons_list[month])