# Преобразование строки чисел (каждый элемент имеет тип str) в список чисел (каждый элемент имеет тип float)

# Строка чисел
str_numbers = '-1 2 3';

# Список чисел, каждое из которых имеет тип str
list_str_numbers = str_numbers.split();

# Преобразование типа str в тип float
list_float_numbers = [];
for i in range(len(list_str_numbers)):
    list_float_numbers.append(float(list_str_numbers[i]));

print(f'Полученный список чисел типа str: {list_str_numbers}');
print(f'Полученный список чисел типа float: {list_float_numbers}');