# Напишите программу, которая содержит внешнюю функцию.
# Функция запрашивает у пользователя два целых числа a и b (гарантируется, что a <= b).
# Функция должна вывести все простые числа в диапазоне от a до b включительно

import math

def simple_range(left, right):
    list_simple=[]; # список простых чисел в диапазоне от числа left до числа right включительно
    
    is_simple=True;
    for number in range(left,right+1):
        # Числа 0 и 1 не являются простыми
        if number < 2:
            continue;
        for divider in range(2, math.isqrt(number)+1):
            if(number % divider == 0):
                is_simple = False;
                break;
    if(is_simple == True):
        list_simple.append(number);
    return list_simple;

# Ввод чисел a и b
a = int(input('Введите первое натуральное число: '));
b = int(input('Введите второе натуральное число: '));

simple_list = simple_range(a,b);
len_simple_list = len(simple_list);

print(f'Количество простых чисел в диапазоне [{a}, {b}] равно {len_simple_list}: {simple_list}');

