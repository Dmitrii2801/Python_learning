# Применение условного оператора (определение количества одинаковых цифр, встречающихся в числе)
# Развитие задачи в папке 3_Cycles, файле Lesson_2

number = int(input('Введите любое натуральное трехзначное число: '))
check_number = int(input('Введите цифру, которую требуется найти в трехзначном числе: '))

# Разделение числа на десятичные знаки (число 123 - на цифры 1, 2, 3)
digit_1 = int(number/100%10); # разряд сотен
digit_2 = int(number/10%10); # разряд десятков
digit_3 = number%10; # разряд единиц

# Вывод десятичных разрядов числа
print(digit_1)
print(digit_2)
print(digit_3)

# Обработка условия (проверка наличия цифры check_number в числе number)
if (digit_1 == check_number or digit_2 == check_number or digit_3 == check_number):
    print('Число', number, 'содержит цифру', check_number);
else:
    print('Число', number, 'не содержит цифру', check_number);