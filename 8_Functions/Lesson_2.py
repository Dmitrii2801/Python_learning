# Функция для задания ряда чисел Фибоначчи (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...)

def Fibonacci(n): # n - требуемое количество элементов в списке
    array_Fibonacci = [0,1]; # первые два числа в ряду Фибоначчи
    for i in range(n):
        sum_a_last = sum(array_Fibonacci[len(array_Fibonacci)-2:len(array_Fibonacci)]);
        array_Fibonacci.append(sum_a_last);
    return [array_Fibonacci];

quantity = int(input('Введите требуемое количество чисел Фибоначчи: '));
Fib = Fibonacci(quantity);

print(f'Ряд из {quantity} чисел Фибоначчи: {Fib}');