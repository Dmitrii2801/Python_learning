# Информация для базы данных
# Пользователь вводит информацию о себе (имя, пол, возраст, город, профессия)
# Создать словарь из данных о пользователе. Дополнить словарь фамилией через метод .get().
# Изменить город на другой. Добавить ключ-значение по изучению Python (Да - True / Нет - False)

# Ввод информации о пользователе
name = input('Введите ваше имя: ');
sex = input('Введите ваш пол: ');
age = int(input('Укажите ваш возраст: '));
city = input('Укажите город проживания: ');
profession = input('Укажите вашу профессию: ')

# Создание словаря на основе данных о пользователе
user = {
    'name': name,
    'sex': sex,
    'age': age,
    'city': city,
    'profession': profession    
}

print(f'Изначальный словарь user: {user}');

# Добавление информации о фамилии пользователя
user['surname']=user.get('surname', input('Введите вашу фамилию: '));

# Смена города проживания
user['city'] = input('Укажите иной город проживания: ');

# Добавление ключа-значения по изучению Python
answer = input('Вы изучаете язык программирования Python? (Да / Нет) ');
if answer=='Да':
    user['learning-Python'] = user.get('learning-Python', True);
else:
    user['learning-Python'] = user.get('learning-Python', False);

print(f'Дополненный словарь user: {user}');

# Удаление ключа-значения города проживания
user.pop('city');

print(f'Словарь user (без ключа city): {user}');

# Вывод ключа и значения из словаря в цикле for
for key, value in user.items():
    print(f'Ключ {key}, значение {value}');