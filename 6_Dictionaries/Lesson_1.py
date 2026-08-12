# Создание словарей
# Создать объект с параметрами, которые необходимо находить по ключ-значению
# Данные объекты создаются с помощью словарей (dictionaries)

# Поиск научной публикации (критерии поиска: название статьи, автор, аффилиация, год выпуска, журнал, количество страниц, ключевые слова)
research_paper = {
    'name': 'Modeling of control system for Coriolis mass flowmeter in two-phase flow conditions',
    'author': 'D. Goncharov',
    'affiliation': 'South Ural State University',
    'year': 2025,
    'journal': 'Proceedings of APEIE-2025',
    'pages': 6,
}

print(f'Информация о найденной публикации: {research_paper}');

# Вывести характеристику объекта по ключ-значению
key = input('Введите ключ-значение: '); # name, author, affiliation, year, journal, pages
print(research_paper.get(key)); # или print(research_paper['key'])

# Изменить словарь (дополнить, удалить элементы)
research_paper['keywords'] = 'flowmeter', 'control system', 'algorithm', 'two-phase flow';
research_paper.pop('pages');

print(f'Информация о найденной публикации (после рецензирования): {research_paper}');

# Проверить, упоминается ли в ключевых словах (keywords) конкретный термин
keyword = input('Введите искомое ключевое слово: ');
if(keyword in research_paper['keywords']):
    print(f'Ключевое слово "{keyword}" встречается в публикации "{research_paper['name']}"');
else:
    print(f'Ключевое слово "{keyword}" не найдено');