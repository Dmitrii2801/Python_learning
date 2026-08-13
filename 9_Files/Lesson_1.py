# Работа с csv-файлами. Чтение данных из файла и обработка этих данных

import pandas as pd # библиотека для работы с таблицами (в том числе с файлами .csv)
import numpy as np # библиотека для математических операций со списками
import matplotlib.pyplot as plt # библиотека для построения
# графиков (https://metanit.com/python/matplotlib/), (https://habr.com/ru/articles/1028868/)

file_path1 = '9_Files\data\Coil.csv'; # путь к файлу_1
file_path2 = '9_Files\data\est_A.csv'; # путь к файлу_2

Coil_df = pd.read_csv(file_path1, header=None); # считать данные из csv-файла, расположенного по заданному пути
est_A_df = pd.read_csv(file_path2, header=None); # считать данные из csv-файла, расположенного по заданному пути

Coil = Coil_df[0].tolist(); # перенести данные из первого столбца (нумерация с 0) в список под названием Coil
est_A = est_A_df[0].tolist(); # перенести данные из первого столбца (нумерация с 0) в список под названием est_A

# Временной диапазон для построения графиков
t0 = 0; # начало записи
dt = 1e-3; # период дискретизации
t_stop = dt*len(Coil);

window_size = 50; # длина блочного окна метода матричных пучков
dt_est = dt*window_size; # период обновления оценок

t = np.arange(t0,t_stop,dt); # временной диапазон для наблюдения
t_est = np.arange(t0,t_stop-dt_est,dt_est);

# Построение графиков

# plt.plot(t, Coil);
# plt.grid()
# plt.show()