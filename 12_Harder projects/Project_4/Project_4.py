# Генератор простых чисел в диапазоне [2, N]

import math

# Функция, которая проверяет, является ли элемент числом
def is_number(limit:str):
    try:
        N_int = int(limit);
        print('Элемент является числом');
    except ValueError:
        print('Введенный элемент не является числом!');
        N_int = int(input('Введите натуральное число (>= 2) заново: '));
    if(N_int < 2):
        print('Введенный элемент меньше 2');
        N_int = int(input('Введите натуральное число (>= 2) заново: '));   
    return N_int;

# Функция проверки числа из списка на простоту
def is_prime(number:int):
    for j in range(2, math.isqrt(number)+1):
        if (number % j) == 0:
            return False;
    return True;

N_str = input('Введите натуральное число (>= 2): ');
N_int = is_number(N_str);

list_primes = []; # список простых чисел в диапазоне [2, N]
list_not_primes = []; # список чисел в диапазоне [2, N], которые не являются простыми

# Цикл генерации простых чисел в диапазоне [2, N]
for number in range(2,N_int+1):
    if(is_prime(number)):
        list_primes.append(number);
    else:
        list_not_primes.append(number);

# Вывод данных
print(f'Список простых чисел из диапазона [2, {N_int}]: {list_primes}');
print(f'Список чисел из диапазона [2, {N_int}], которые не являются простыми: {list_not_primes}');