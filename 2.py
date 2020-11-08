user_time = int(input('Сколько секунд нужно перевести в часы и минуты? '))
hours = user_time // 3600
minutes = (user_time - hours * 3600) // 60
seconds = user_time - hours * 3600 - minutes * 60
count_time = f'{user_time} секунд - это {hours}ч:{minutes}мин:{seconds}сек'
print(count_time)

