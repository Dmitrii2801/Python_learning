# Удаление всех простых чисел из массива

import math
import random

n = int(input('Введите количество элементов в массиве: '));
x_initial = [0]*n;
x_result = [0]*n;
x_simple = [];

for i in range(n): # заполнение массива
    x_initial[i] = random.randint(1,100);
    x_result[i] = x_initial[i];

for k in range(n): # проверка на простоту и удаление простых чисел из массива
    is_simple = True;
    for j in range(2, math.isqrt(x_initial[k])):
        if(x_initial[k]%j==0):
            is_simple = False;
            break;
    if(is_simple == True):
        x_simple.append(x_initial[k]);
        x_result[k] = [];

print('Исходный массив: ', x_initial);
print('Результирующий массив (без простых чисел): ', x_result);
print('Простые числа из массива x:', x_simple);