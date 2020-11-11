now = int(input('Какой ваш результат сейчас?'))
goal = int(input('Какого результата вы хотите достичь?'))
day = 1
while goal > now:
    now = now + now * 0.1
    day += 1
result = f'На {day}-й день спортсмен достиг результата — не менее {goal} км.'
print(result)