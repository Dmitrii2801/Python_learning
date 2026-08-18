# Написать программу, которая содержит внешнюю функцию. Функция запрашивает у
# пользователя строку и символ. Программа должна подсчитать, сколько раз данный
# символ встречается в строке (регистр учитывается, т.е. 'A' и 'a' – разные символы).
# Затем программа должна вывести новую строку, в которой все вхождения этого символа
# заменены на звёздочку *. Например, для строки "hello" и символа "l" результат
# будет "he**o". Использовать только методы строк (без регулярных выражений)

# Функция для подсчета количества повторений символа symbol в строке sentence
def count_string(sentence:str, symbol:str):
    list_letters=[]; # количество повторений символов symbol в строке sentence
    
    # Форматирование строки, преобразование ее в список
    list_sentence = list(sentence.strip().split());
    words = [];
    letters = [];
    
    # Подсчет количества повторений символа symbol в строке sentence
    for i_words in range(len(list_sentence)):
        words.append(list_sentence[i_words]);
        for j_letters in range(len(words[i_words])):
            letters.append(words[j_letters]);
    print(words);
    print(letters);

sentence='ты ns';
symbol='ы';
count_string(sentence, symbol);
