def summary():
    ex = False
    result = 0
    while not ex:
        numbers = input('Введите числа через пробел или q для выхода: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res_line += int(num)
        result += res_line
    return result

print(summary())

#сделала дополнительно то же, но для умножения, чтобы получше запомнить)

def multiplication():
    ex = False
    result = 1
    while not ex:
        numbers = input('Введите числа через пробел или q для выхода: ').split()
        res_line = 1
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res_line *= int(num)
        result *= res_line
    return result

print(multiplication())