# Создать функцию, в которую из внешней среды передаются ключ-значения и элементы словаря. Для этого при задании
# аргументов в функции поставить **kwargs - ссылка на именованные аргументы.
# Все аргументы **kwargs для функции являются словарем, т.к. записываются в фигурных {} скобках

def print_info(**kwargs): # kwargs - keyword arguments (именованные аргументы)
    print(f'Передаваемые аргументы: {kwargs}')

print_info(country='Russia', city='Saint Petersburg', imperor='Peter I');

# В одну и ту же функцию можно передавать и *args, и **kwargs
# def function_name(*args, **kwargs): # как это будет выглядеть
    # body of function;
    # return something;