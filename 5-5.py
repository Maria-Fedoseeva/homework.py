with open('numbers.txt', 'w', encoding='utf-8') as numbers:
    nums = input('Введите целые числа через пробел: ')
    numbers.write('Введенные числа: ' + nums + '\n')
    nums = map(int, nums.split())
    sum_nums = sum(nums)
    numbers.write('Сумма чисел: ' + str(sum_nums))
    print('Сумма введенных чисел: ', sum_nums)
print('Все записанно в файл')