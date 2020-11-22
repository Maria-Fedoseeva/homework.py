my_list = [1, 3, 3, 5, 8, 8, 13, 7, 7, 34, 14]
new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)