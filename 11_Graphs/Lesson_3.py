# Построение диаграммы рассеяния (ax.scatter()). Нужна для поиска корреляций между несколькими случайными
# величинами. Например, зависимость массы тела человека от его роста

# Каждая точка на графике в данном случае будет представлять собой один объект

import numpy as np
import matplotlib.pyplot as plt

# Генерация quantity (количество точек) случайных значений
quantity = 50; # 50 случайных значений
height = np.random.normal(170, 10, quantity); # значения в диапазоне (170 +- 10) см
weight = height*0.4 + np.random.normal(0, 5, quantity);

# Построение графика
fig, ax = plt.subplots()
ax.scatter(height, weight) # зависимость массы тела человека от его роста
ax.set_title('Зависимость массы тела человека от его роста')
ax.set_xlabel('Рост, см')
ax.set_ylabel('Масса тела, кг')
ax.grid()

plt.show()