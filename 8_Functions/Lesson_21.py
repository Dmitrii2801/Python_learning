# Написать программу, которая содержит внешнюю функцию
# Функция запрашивает у пользователя строку, содержащую натуральные числа.
# Программа должна преобразовать эту строку в список чисел, а затем создать
# и вывести новый список, в котором все дубликаты удалены, но порядок первого
# появления элементов сохранен

# Функция для поиска повторений в списке
def pop_duplicates(string:str):
    list_string = list(string.split());
    numbers = [];
    unique_numbers = [];
    
    for i in range(len(list_string)):
        numbers.append(int(list_string[i]));
    
    for j in range(len(numbers)):
        if(numbers[j] not in unique_numbers):
            unique_numbers.append(numbers[j]);
    
    print(f'Изначальный список: {numbers}');
    print(f'Результирующий список (с удаленными дубликатами): {unique_numbers}');

string_nums = '1 2 3 3 3';
pop_duplicates(string_nums);