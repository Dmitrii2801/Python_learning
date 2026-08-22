# Написать программу, которая содержит внешнюю функцию. Функция запрашивает у пользователя
# строку. Программа должна определить, является ли введенная строка палиндромом.
# Если введенная строка является палиндромом, вывести True. В противном случае вывести False

# Функция для проверки строки на палиндром
def palindrome(string:str):
    symbols = list(string.lower().strip()); # разделение строки на символы
    symbols_without_spaces = [];
    for j in range(len(symbols)):
        if(symbols[j] != ' '):
            symbols_without_spaces.append(symbols[j]);
    if(symbols_without_spaces == symbols_without_spaces[::-1]):
        print('Строка является палиндромом');
    else:
        print('Строка не является палиндромом');

string1 = 'А роза упала на лапу Азора';
palindrome(string1);

string2 = 'А розы упали на лапу Азора';
palindrome(string2);
