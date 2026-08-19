# Написать программу, которая содержит внешнюю функцию. Функция запрашивает у
# пользователя строку и символ. Программа должна подсчитать, сколько раз данный
# символ встречается в строке (регистр учитывается, т.е. 'A' и 'a' – разные символы).
# Затем программа должна вывести новую строку, в которой все вхождения этого символа
# заменены на звёздочку *. Например, для строки "hello" и символа "l" результат
# будет "he**o". Использовать только методы строк (без регулярных выражений)

# Функция для подсчета количества повторений символа symbol в строке sentence
def count_string_letters(sentence:str, symbol:str):    
    # Форматирование строки, преобразование ее в список
    list_sentence = list(sentence.strip().split());
    
    letters = []; # список для отдельных букв каждого слова из строки sentence
    words_with_symbol = []; # слова, в которых хотя бы 1 раз встречается символ symbol
    symbol_repeat=0; # количество повторений символа symbol во всех словах строки sentence
    
    result_words = []; # список слов с заменой символа symbol на символ *
    
    # Подсчет количества повторений символа symbol в строке sentence
    for i_words in range(len(list_sentence)): # i_words - количество слов в строке sentence
        letters = list(list_sentence[i_words]); # разделение каждого слова на отдельные буквы
        flag_letter = True; # индикатор наличия символа symbol в любом слове из строки sentence
        for j_letters in range(len(letters)): # проверка наличия символа symbol в каждом слове строки sentence
            if(symbol in letters[j_letters]): # если символ есть в списке букв слова,
                symbol_repeat += 1; # прибавить 1 к количеству символов symbol в строке sentence,
                letters[j_letters] = '*';
                if(flag_letter == True): # и если до этого символ не встречался в этом слове,
                    words_with_symbol.append(list_sentence[i_words]); # добавить слово в список words_with_symbol
                    flag_letter = False; # если символ встретится в слове еще раз, больше не добавлять это слово
        result_words.append(''.join(letters)); # заполнение списка слов с заменой символа symbol на символ *
        result_sentence = ' '.join(result_words); # результирующая строка с заменой символа symbol на символ *
        flag_letter = True; # вернуть индикатор в True (для других слов)
    
    # Вывод данных
    match symbol_repeat:
        case m if (symbol_repeat == 0):
            print(f'Символ {symbol} не встречается в строке {sentence}');
        case m if (symbol_repeat == 1 or symbol_repeat > 5):
            print(f'Символ {symbol} встречается {symbol_repeat} раз в словах {words_with_symbol}');
        case m if (symbol_repeat > 1 and symbol_repeat < 5):
            print(f'Символ {symbol} встречается {symbol_repeat} раза в словах {words_with_symbol}');
    
    print(f'Результирующая строка с заменой символа "{symbol}" на символ *: {result_sentence}')

# Ввод данных
sentence='Проходите, пожалуйста, дорогой почтальон Печкин'; # строка
symbol='П'; # искомый символ

# Применение функции count_string_letters
count_string_letters(sentence, symbol);