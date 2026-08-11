# Вводится строка full_name с пробелами по краям и буквами в разном регистре.
# Привести запись к нормальному виду: убрать пробелы по краям; первую букву сделать заглавной, остальные - строчными
# Вывести первый и последний символ в строке через точку

full_name = 'dImA iS tHe BesT PytHoN DeveLOpeR';

# Исправление записи (удаление лишних пробелов, замена регистров для букв)
full_name_corrected = full_name.capitalize().strip();
length_corrected = len(full_name_corrected);

print(f'Запись до исправления {full_name}');
print(f'Запись после исправления {full_name_corrected}');

# Вывод первого и последнего символа исправленной записи через точку
print(f'{full_name_corrected[0]}.{full_name_corrected[length_corrected-1]}');