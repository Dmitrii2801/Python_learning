# Пропуск четных элементов при переборе

import random

n = int(input('Введите количество элементов массива: '));
x = [0]*n;

for i in range(1,n+1):
    if (i % 2 == 0):
        continue;
    x[i] = random.randint(1,100);
    print(i, '-ый элемент:', x[i], sep='', end='\n');