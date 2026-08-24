"""
Напишите программу, которая запрашивает у пользователя строку, содержащую числа, разделённые пробелами. Программа должна:

1. Разбить строку на отдельные элементы.

2. С помощью внешней функции parse_number() попытаться преобразовать каждый элемент в число с плавающей точкой.
Если преобразование невозможно (например, элемент содержит буквы), функция должна возвращать None, а программа — выводить предупреждение.

3. Собрать все успешно преобразованные числа в список.

4. С помощью другой внешней функции calculate_average() вычислить среднее арифметическое этих чисел. Если чисел нет, вывести сообщение об ошибке.

5. В основной программе использовать цикл для обработки ввода (например, пока пользователь не введёт пустую строку) и список для хранения всех чисел
за все итерации (или обрабатывать каждую строку отдельно — по выбору).
"""

list_float_numbers = [];

# Попытка преобразования элементов строки в тип float
def parse_number(string_numbers:str):
    list_string_numbers = string_numbers.split();
    try:
        for numbers_index in range(len(list_string_numbers)):
            list_float_numbers.append(float(list_string_numbers[numbers_index]));
        return list_float_numbers;
    except ValueError:
        print('Невозможно преобразовать символы в тип float')
        return None;

# Попытка расчета среднего арифметического значения элементов типа float списка
def calculate_average(list_float_numbers:list):
    if(list_float_numbers==None):
        raise ValueError('Числа отсутствуют!');
    else:
        average = sum(list_float_numbers)/len(list_float_numbers);
        return average;

# Ввод строки с числами (с использованием цикла)
input_numbers = [];
while(True):
    element = input(f'Введите элемент: ');
    if(element != ''):
        input_numbers.append(element);
    else:
        break;

string_numbers = ' '.join(input_numbers);

# Применение функций
list_float_numbers=parse_number(string_numbers); # попытка преобразования элементов строки в тип float
average = calculate_average(list_float_numbers); # попытка рассчитать среднее арифметическое значение элементов списка

# Вывод данных
print(f'Среднее арифметическое значение элементов списка {list_float_numbers} равно {average}');