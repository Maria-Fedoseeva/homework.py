def my_func(num_1, num_2, num_3):
    try:
        my_list = [num_1, num_2, num_3]
        my_list.pop(my_list.index(min(my_list)))
        return sum(my_list)
    except TypeError:
        return 'Check number'
#объясните, пожалуйста, в чем смысл писать TypeError? Я в числах заменила одну на букву, вышла NameError, но это именно
#ошибка в исполнении функции, и когда я Type сменила на Name, это ничего не изменило. Зачем мы тогда это пишем?

print(my_func(1, 2, 4))