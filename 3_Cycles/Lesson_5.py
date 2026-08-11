# Поиск количества повторений конкретной цифры в элементах массива
# Требуется вывести как количество повторений цифры в элементах массива, так и все элементы
# массива, в которых встречается эта цифра
# Развитие задачи из папки 3_Cycles, файла Lesson_2

import random # импорт библиотеки для генератора случайных чисел

n = int(input('Введите количество элементов массива: '));
check_number = int(input('Введите цифру, которую требуется найти во всех элементах массива: '))
x = [0]*n; # массив из нулей
decades = [0]*n; # массив из нулей
x_digit = []; # массив для десятичных разрядов числа number
x_number = []; # массив для элементов массива, в которых встречается цифра check_number
x_check = []; # массив для одинаковых десятичных разрядов числа number
flag_number = 0; # индикатор наличия элемента массива с цифрой check_number в массиве x_number

for i in range(n):
    x[i] = random.randint(1,10000); # заполнение массива n элементами в диапазоне (1...1000)
    decades[i] = len(str(x[i])); # определение разрядности числа
    num_digit = 10**(decades[i]-1); # параметр для разделения на десятичные разряды
    for j in range(decades[i]): # разделение на десятичные разряды
        digit = int(x[i]/num_digit%10);
        x_digit.append(digit);
        num_digit = num_digit/10;
        if(digit == check_number):
            if(flag_number==0):
                x_number.append(x[i]);
                flag_number = flag_number + 1;
            x_check.append(digit);
    flag_number = 0;

print('Исходный массив: ', x, sep=''); # вывод массива x с десятичными знаками числа number
print('Массив чисел с цифрой ', check_number, ': ', x_number, sep='');
print(x_check); # вывод массива x_check со всеми десятичными знаками, которые равны числу check_number
x_check_len = len(x_check); # количество повторений цифры check_number в массиве x

# Обработка условия (поиск количества повторений цифры check_number в числе number)
match x_check_len:
    case m if (x_check_len == 0):
        print('Массив', x, 'не содержит цифру', check_number);
    case m if (x_check_len == 1 or x_check_len > 5):
        print('Массив', x, 'содержит цифру', check_number, x_check_len, 'раз');
    case m if (x_check_len > 1 and x_check_len < 5):
        print('Массив', x, 'содержит цифру', check_number, x_check_len, 'раза');