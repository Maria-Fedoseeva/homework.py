def my_div(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
        print(answer)
    except ValueError:
        print('Ошибка числа')
    except ZeroDivisionError:
        print('Деление на ноль!')

number_1 = input('Введите первое число: ')
number_2 = input('Введите второе число: ')

my_div(number_1, number_2)


