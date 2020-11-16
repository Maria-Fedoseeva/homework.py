def personal_info(**kwargs):
    return kwargs

print(personal_info(
    name = input('Имя: '),
    surname = input('Фамилия: '),
    year = input('Год рождения: '),
    city = input('Город проживания: '),
    email = input('Email: '),
    phone = input('Телефон: ')
))