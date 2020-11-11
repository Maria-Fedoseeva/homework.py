proceeds = int(input('Введите выручку компании: '))
costs = int(input('Введите издержки компании: '))

profit = proceeds - costs

if profit > 0:
    print('Прибыль компании: ', profit)
    #до того, как подглядела в урок, рентабильность и прибыль на каждого были вне if
    print('Рентабельность:', profit / proceeds)
    people = int(input('Сколько сотрудников у вас работает?'))
    print(f'Прибыль на одного сотрудника: {int(profit / people)}')
elif result < 0:
    print('Убыток компании составляет: ', profit)
else:
    print('Компания работает в 0')