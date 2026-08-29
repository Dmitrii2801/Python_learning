# Калькулятор среднего арифметического значения

# Попытка преобразования элементов строки в тип float
list_float_numbers = []; # список для элементов строки string_numbers, которые преобразованы в тип float
def parse_number(string_numbers:str):
    list_string_numbers = string_numbers.split(); # разделение строки на отдельные элементы
    try:
        for numbers_index in range(len(list_string_numbers)):
            list_float_numbers.append(float(list_string_numbers[numbers_index])); # преобразовать каждый элемент типа str в списке в тип float
        return list_float_numbers; # вернуть список из элементов типа float
    except ValueError: # если хотя бы один элемент строки не будет являться числом,
        print('Невозможно преобразовать символы в тип float')
        return None; # вместо списка вывести None (ничего)

# Попытка расчета среднего арифметического значения элементов типа float списка
def calculate_average(list_float_numbers:list):
    if(list_float_numbers==None): # если список элементов типа float пуст,
        raise ValueError('Числа отсутствуют!'); # вывести ошибку, что числа отсутствуют - невозможно рассчитать среднее арифметическое значение
    else: # если список не пуст,
        average = sum(list_float_numbers)/len(list_float_numbers); # рассчитать среднее арифметическое значение
        return average; # и вернуть его

# Ввод строки с элементами (с использованием цикла)
input_numbers = []; # список элементов типа str, введенных с клавиатуры
while(True):
    element = input(f'Введите элемент: ');
    if(element != ''): # если элемент не является пустой строкой,
        input_numbers.append(element); # добавить его в список input_numbers
    else: # в обратном случае
        break; # выйти из цикла

string_numbers = ' '.join(input_numbers); # преобразовать список элементов типа str в строку (через метод .join())

# Применение функций
list_float_numbers=parse_number(string_numbers); # попытка преобразования элементов строки в тип float
average = calculate_average(list_float_numbers); # попытка рассчитать среднее арифметическое значение элементов списка

# Вывод данных
print(f'Среднее арифметическое значение элементов списка {list_float_numbers} равно {average}');