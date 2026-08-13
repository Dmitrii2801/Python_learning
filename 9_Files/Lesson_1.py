# Работа с csv-файлами. Чтение данных из файла и вывод этих данных в терминал

import pandas as pd # библиотека для работы с таблицами (в том числе с файлами .csv)

file_path1 = '9_Files\data_ex\Coil.csv'; # путь к файлу_1
file_path2 = '9_Files\data_ex\Driver.csv'; # путь к файлу_1
file_path3 = '9_Files\data_ex\est_A.csv'; # путь к файлу_2

Coil_df = pd.read_csv(file_path1, header=None); # считать данные из csv-файла, расположенного по заданному пути
Driver_df = pd.read_csv(file_path2, header=None); # считать данные из csv-файла, расположенного по заданному пути
est_A_df = pd.read_csv(file_path3, header=None); # считать данные из csv-файла, расположенного по заданному пути

Coil = Coil_df[0].tolist(); # перенести данные из первого столбца (нумерация с 0) в список под названием Coil
Driver = Driver_df[0].tolist(); # перенести данные из первого столбца (нумерация с 0) в список под названием Driver
est_A = est_A_df[0].tolist(); # перенести данные из первого столбца (нумерация с 0) в список под названием est_A

print(f'Список данных из файла Coil.csv: {Coil}');
print(f'Список данных из файла Driver.csv: {Driver}');
print(f'Список данных из файла est_A.csv: {est_A}');