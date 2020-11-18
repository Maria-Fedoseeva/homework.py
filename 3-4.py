def my_pow_func(x, y):
    try:
        ans = x ** y
    except TypeError:
        return 'Enter float'
    return ans

# 2
def my_pow_func_2(x, y):
    try:
        x, y = float(x), int(y)
        res = x
        for i in range(abs(y)-1):
            res *= x
        return 1 / res
    except ValueError:
        return 'Check value'


print(my_pow_func(10, -4))
print(my_pow_func_2(10, -3))