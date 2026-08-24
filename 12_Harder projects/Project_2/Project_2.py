# Метод обработки данных о температуре за конкретный промежуток времени (в днях)

import numpy as np
import matplotlib.pyplot as plt

# Функция для преобразования данных по температуре типа str в тип float
def validate_temperature(days_count:int, string_value:str):
    try:
        float_value = float(string_value); # преобразовать элемент типа str в тип float
    except ValueError: # если введено не число, а строка
        print('Введено некорректное значение температуры!');
        string_value = input(f'Введите корректное значение температуры для {days_count} дня: '); # ввести корректное значение температуры
        float_value = float(string_value); # преобразовать новое значение типа str в тип float
    return float_value; # вернуть значение типа float


# Ввод данных с клавиатуры

days_count = 1; # счетчик дней
days = []; # список дней (для построения графика)
temperature = []; # список вещественных значений температуры (для построения графика)

# Цикл для ввода значений температуры
while(True):
    str_temperature_value = input(f'Введите значение температуры в {days_count} день: '); # ввод значений типа str
    
    if(str_temperature_value == ''): # если элемент является пустой строкой,
        break; # выйти из цикла
    
    # Применение функции для преобразования типов
    float_temperature_value = validate_temperature(days_count, str_temperature_value);
    
    # Добавить новое значение температуры в список
    temperature.append(float_temperature_value);
    
    # Перейти к вводу данных для нового дня
    days.append(days_count);
    days_count += 1;

# Обработка данных о температуре с помощью numpy

# Расчет среднего арифметического значения температуры
avg_temp = round(np.average(temperature),2);

# Расчет среднего квадратического отклонения температуры
std_temp = round(np.std(temperature),2);

# Расчет минимального и максимального значения температуры
min_value_temp = np.min(temperature);
max_value_temp = np.max(temperature);

# Вывод полученных данных
print(f'Значения температуры на протяжении {days_count} дней: {temperature}');

print(f'Среднее арифметическое значение температуры за {days_count} дней: {avg_temp}');

print(f'Среднее квадратическое отклонение температуры за {days_count} дней: {std_temp}');

print(f'Минимальное значение температуры за {days_count} дней: {min_value_temp}');
print(f'Максимальное значение температуры за {days_count} дней: {max_value_temp}');

# Построение графиков

fig, ax = plt.subplots(nrows=2, ncols=2)

ax[0, 0].plot(days, temperature, color='red', linewidth=2.5)
ax[0, 0].set_title('Линейный график')
ax[0, 0].set_xlabel('Номер дня')
ax[0, 0].set_ylabel('Температура, С')

ax[0, 1].scatter(days, temperature, color='blue')
ax[0, 1].set_title('Диаграмма рассеяния')
ax[0, 1].set_xlabel('Номер дня')
ax[0, 1].set_ylabel('Температура, С')

ax[1, 0].bar(days, temperature, color='yellow')
ax[1, 0].set_title('Столбчатая диаграмма')
ax[1, 0].set_xlabel('Номер дня')
ax[1, 0].set_ylabel('Температура, С')

ax[1, 1].hist(temperature, bins=3, color='green')
ax[1, 1].set_title('Гистограмма распределения')
ax[1, 1].set_xlabel('Номер интервала')
ax[1, 1].set_ylabel('Количество значений в интервале')

plt.show()
plt.tight_layout()