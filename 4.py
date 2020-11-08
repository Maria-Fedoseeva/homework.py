# Тоже подглядела в интернете, но это не сработало. В итоге подглядела в разборе на уроке.
#n = int(input('Введите целое положительное число: '))
# max_count = n % 10
# n = n // 10
# while n > 0:
#     if n % 10 > max_count:
#         max_count = n % 10
#         n = n // 10
# result = f'Наибольшая цифра в числе: {max_count}'
# print(result)

n = int(input('Введите целое положительное число: '))
current_max = 0
num = n

while num > 0:
    digit = num % 10
    if digit > current_max:
        current_max = digit
        if current_max == 9:
            break
    num = num // 10

result = f'Наибольшая цифра в числе: {current_max}'
print(result)