# Обращение к индексам строки

language = 'Python';
length = len(language);

for i in range(length):
    print(i, '-ый символ: ', language[i], sep='');
    
# Обращение по отрицательным индексам - то же самое, что и чтение строки наоборот
print(language[-1]); # n
print(language[-2]); # o
print(language[-3]); # h
print(language[-4]); # t
print(language[-5]); # y
print(language[-6]); # P