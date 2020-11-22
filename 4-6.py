#1
from itertools import count, cycle

for i in count(int(input('Введите стартовое число: '))):
    print(i)
#2
my_list = ['тот', 'прав,', 'кто', 'прав,']
iter = cycle(my_list)
stop = ''
while stop != 'q':
    print(next(iter), end= '')
    stop = input()