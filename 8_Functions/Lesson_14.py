# Написать программу, которая содержит внешнюю функцию.
# Функция запрашивает у пользователя два целых числа a и b (гарантируется, что a <= b).
# Функция должна вывести все простые числа в диапазоне от a до b включительно

import math

# Функция для определения количества простых чисел в диапазоне натуральных чисел от a до b включительно
def simple_range(left:int, right:int):
    list_simple=[]; # список простых чисел в диапазоне от числа left до числа right включительно
    
    # Проверка чисел на простоту
    for number in range(left,right+1):
        is_simple=True;
        # Числа 0 и 1 не являются простыми
        if number < 2:
            continue;
        # Проверка делимости числа
        for divider in range(2, math.isqrt(number)+1):
            if(number % divider == 0):
                is_simple = False;
                # break;
        if(is_simple == True): # если число простое,
            list_simple.append(number); # записываем его в список
    
    return list_simple; # выходной параметр функции: список простых чисел

# Ввод чисел a и b
a = int(input('Введите первое натуральное число: '));
b = int(input('Введите второе натуральное число: '));

simple_list = simple_range(a,b); # список простых чисел в диапазоне чисел от a до b включительно
len_simple_list = len(simple_list); # количество простых чисел

print(f'Количество простых чисел в диапазоне [{a}, {b}] равно {len_simple_list}: {simple_list}');