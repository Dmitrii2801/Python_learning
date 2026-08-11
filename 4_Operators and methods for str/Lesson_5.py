# Выводится строка с пробелами по краям. Требуется убрать пробелы и вывести полезную часть надписи
# Если после очистки пробелов строка пустая, вывести EMPTY. Если в строке находится spam, вывести BLOCKED

information = input('Введите строку: ');

print(f'Информация (с пробелами): {information}');

# Удаление пробелов по краям строки
useful_information = information.strip();

# Обработка условия для строки
if(len(useful_information) == 0):
    print('EMPTY');
elif (useful_information == 'spam'):
    print('BLOCKED');
else:
    print(f'Полезная информация: {useful_information}');