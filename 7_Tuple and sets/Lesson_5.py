# Задан список слов:
# 1) вывести количество уникальных (неповторяющихся) слов в нем (через множество)
# 2) проверить, есть ли в множестве слово 'tuple'
# 3) добавить в множество слово 'loop'
# 4) удалить слово 'list' из множества
# 5) преобразовать полученное множество к списку, вывести список

words_list = ["python", "code", "list", "python", "set", "code", "tuple"]; # список слов

words_set = set(words_list); # преобразование списка ко множеству (прямая задача)

print(f'Изначальный список: {words_list}');
print(f'Изначальное множество: {words_set}');

quantity_unique_words = len(words_set); # количество уникальных слов в списке words

print(f'Количество уникальных слов в списке {words_list}: {quantity_unique_words}');

# Проверка наличия слова 'tuple' в множестве
if('tuple' in words_set):
    print(f'Слово tuple обнаружено в множестве {words_set}');
else:
    print(f'Слово tuple не обнаружено в множестве {words_set}');

# Добавить слово 'loop' в множество
words_set.add('loop');

# Удалить слово 'list' из множества
words_set.remove('list');

# Преобразование множества к списку (обратная задача)
words_new_list = list(words_set);

print(f'Результирующий список: {words_new_list}');
print(f'Результирующее множество: {words_set}');