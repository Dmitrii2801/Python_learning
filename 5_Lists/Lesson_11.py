# Списочные выражения-1 (list comprehension). Простые примеры

import random

# Вариант создания списков, использовавшийся ранее

n=5;
numbers=[];

for i in range(n):
    if(i %2 != 0):
        numbers.append(i);

print(f'Первый вариант генерации списка: {numbers}');

# Упрощенный вариант создания списков (в одну строчку)

improve_numbers = [i for i in range(n) if i %2 != 0];

print(f'Второй вариант генерации списка: {improve_numbers}');