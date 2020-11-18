my_list = [1, 6, 3, 5, 8, 2, 13, 7, 21, 34, 14]
new_list = [num for i, num in enumerate(my_list) if my_list[i] > my_list[i - 1] and i != 0]
print(new_list)
