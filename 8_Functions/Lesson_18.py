# Написать программу, которая содержит внешнюю функцию. Функция запрашивает у
# пользователя натуральные числа numbers и цифру number. Программа должна подсчитать,
# сколько раз цифра number встречается в каждом введенном числе. Программа работает,
# пока пользователь не введет число, в котором не встречается цифра number. После каждого
# ввода числа выводится сообщение "Число numbers содержит цифру number n раз" или (в случае ошибки)
# "Число numbers не содержит цифру number"

# Функция для подсчета количества повторений символа symbol в строке sentence
def count_numbers(check_number:int):    
    list_numbers = [];
    
    while(True):
        numbers = int(input());
        digit_repeat = 0; # количество цифр check_number в числе numbers
        decades = len(str(numbers));
        num_digit = 10**(decades-1);
        flag_number = True;
        for j in range(decades):
            digit = int(numbers/num_digit%10);
            num_digit /= 10;
            if(digit == check_number):
                digit_repeat += 1;
                if(flag_number == True):
                    list_numbers.append(numbers);
                    flag_number = False;
        flag_number = True;
        match digit_repeat:
            case m if (digit_repeat == 0):
                print(f'Цифра {check_number} не встречается в числе {numbers}');
                break;
            case m if (digit_repeat == 1 or digit_repeat > 5):
                print(f'Цифра {check_number} встречается {digit_repeat} раз в числе {numbers}');
            case m if (digit_repeat > 1 and digit_repeat < 5):
                print(f'Цифра {check_number} встречается {digit_repeat} раза в числе {numbers}');

# Искомая цифра
check_number = 9;

# Применение функции count_numbers
count_numbers(check_number);