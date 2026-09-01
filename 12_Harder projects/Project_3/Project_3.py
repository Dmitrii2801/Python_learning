# Построение семейства квадратичных функций

import numpy as np
import matplotlib.pyplot as plt

# Функция для заполнения списка кортежей, каждый из которых содержит коэффициенты квадратичных функций
list_tuples_coefficients = []; # список кортежей, каждый из которых содержит коэффициенты квадратичной функции
def parse_coefficients():
    while(True):
        
        list_float_coefficients = []; # список с вещественными коэффициентами квадратичной функции
        
        string_coefficients = (input('Введите коэффициенты a b c квадратичной функции y = a*x^2 + b*x + c (через пробел): ')).strip();
        if(string_coefficients == ''):
            print('Выход из программы');
            return list_tuples_coefficients;
        
        list_str_coefficients = string_coefficients.split();

        # Условие на количество коэффициентов квадратичной функции
        if(len(list_str_coefficients) < 3):
            print('Введено меньше трех чисел!');
            continue;
        
        # Преобразование типа str в тип float для коэффициентов квадратичной функции
        try:
            for i in range(len(list_str_coefficients)):
                list_float_coefficients.append(float(list_str_coefficients[i]));
            list_tuples_coefficients.append(tuple(list_float_coefficients));
        except ValueError:
            print('Хотя бы один из коэффициентов не является числом, пропускаем');
            continue;

# Применение функции parse_coefficients()
list_tuples_coefficients = parse_coefficients();
print(f'Список семейства квадратичных функций: {list_tuples_coefficients}');

# Построение графиков функций

# Создание графиков
fig, ax = plt.subplots();

# Задание диапазона оси абсцисс (от -10 до 10 с шагом 0.1)
x_data = np.arange(-10, 10, 0.1);

# Расчет данных, наносимых на ось ординат
for tuples in range(len(list_tuples_coefficients)):
    if(list_tuples_coefficients):
        y_data = list_tuples_coefficients[tuples][0] * x_data**2 + list_tuples_coefficients[tuples][1] * x_data + list_tuples_coefficients[tuples][2];
        ax.plot(x_data, y_data, label=f'{tuples+1}-й график');
    else:
        print('Список коэффициентов пуст!');

ax.set_xlabel('Ось абсцисс');
ax.set_ylabel('Ось ординат');
ax.grid(True, linestyle=':', alpha=0.6);
ax.legend()

plt.show()