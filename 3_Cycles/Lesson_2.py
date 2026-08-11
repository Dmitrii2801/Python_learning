# Определение количества одинаковых цифр, встречающихся в числе с разрядностью n
# Развитие задачи из папки 2_If else projects, файла Lesson_4

number = int(input('Введите любое натуральное число: '))
check_number = int(input('Введите цифру, которую требуется найти в заданном числе: '))
decades = len(str(number)); # определение разрядности числа
print(decades);
x = []; # массив для десятичных разрядов числа number
x_check = []; # массив для одинаковых десятичных разрядов числа number

num_digit = 10**(decades-1); # начальное значение параметра для разделения числа на десятичные разряды
# Цикл для разделения числа на десятичные разряды и проверки наличия цифры check_number в числе number
for i in range(decades):
    digit = int(number/num_digit%10); # разделение числа number на десятичные разряды digit
    x.append(digit); # добавление нового разряда в массив
    num_digit = num_digit/10; # обновление параметра для разделения
    if(digit == check_number):
        x_check.append(digit);

print(x); # вывод массива x с десятичными знаками числа number
print(x_check); # вывод массива x_check со всеми десятичными знаками, которые равны числу check_number
x_check_len = len(x_check); # количество повторений цифры check_number в числе number

# Обработка условия (поиск количества повторений цифры check_number в числе number)
match x_check_len:
    case x if (x_check_len == 0):
        print('Число', number, 'не содержит цифру', check_number);
    case x if (x_check_len == 1 or x_check_len > 5):
        print('Число', number, 'содержит цифру', check_number, x_check_len, 'раз');
    case x if (x_check_len > 1 and x_check_len < 5):
        print('Число', number, 'содержит цифру', check_number, x_check_len, 'раза');