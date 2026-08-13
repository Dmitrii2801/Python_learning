# Перенести все простые числа из списка list_numbers во множество set_simple
# Для проверки чисел из списка list_numbers на простоту использовать функцию

# Переименование одной переменной во всех местах выполняется с помощью кнопки F2 при
# нажатии по нужной переменной

import math

# Функция для проверки числа на простоту
def is_simple(number): # number - проверяемое число
    if(number<2): # отрицательные числа и числа 0 и 1 не являются простыми
        return False; # поэтому в этом случае функция возвращает False (число не простое)
    for i in range(2,math.isqrt(number)+1): # проверка делимости числа из списка на разные делители
        if(number % i == 0):
            return False; # если делится без остатка, то не простое
    return True; # в остальных случаях число является простым

list_numbers = list(range(100)); # список с числами от 0 до 99
list_simple = []; # пустой список для простых чисел из списка list_numbers

print(f'Исходный список: {list_numbers}');

for i in range(len(list_numbers)): # перенос простых чисел из списка list_numbers в список list_simple
    if(is_simple(list_numbers[i])): # если число простое,
        list_simple.append(list_numbers[i]); # переносим его из первого списка во второй

set_numbers = set(list_simple); # преобразование списка к множеству

for j in range(len(list_simple)):
    if(list_simple[j] in list_numbers): # если простое число list_simple[j] есть в списке list_numbers,
        list_numbers.remove(list_simple[j]); # удалить его из первого списка

# Вывод полученных данных
print(f'Результирующий список (без простых чисел): {list_numbers}');
print(f'Множество простых чисел из списка: {set_numbers}');