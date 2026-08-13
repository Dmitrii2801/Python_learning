# Задание типов данных аргументов, которые ожидаются на выходе функции

# Пример задачи с расчетом стоимости товара со скидкой
# Потребитель покупает quantity единиц товара, стоимость которого равна price. Если на товар действует (может
# не действовать - True / False) скидка в discount %, уменьшить итоговую стоимость покупки на k %.

# Функция для расчета итоговой стоимости покупки
def get_total_cost(quantity:int, price:float, has_discount:bool, discount:int):
    # Указываемый тип данных через двоеточие после аргумента функции - ожидаемый тип данных данного значения,
    # используется для исключений неопределенностей с типами данных
    
    total_cost = quantity*price; # стоимость quantity единиц товара без учета скидки
    
    if (has_discount == True): # если на товар действует скидка,
        total_cost = total_cost - total_cost*discount/100; # учесть скидку в итоговой стоимости
    return total_cost;

product_quantity = int(input('Введите количество единиц товара для покупки: '));
product_price = 299.99; # стоимость товара (без скидки)
is_discount = True; # действует ли на товар скидка (True - да, False - нет)
if(is_discount == True):
    discount = 30; # размер скидки на товар (%)

total_cost = round(get_total_cost(product_quantity,product_price,is_discount,discount),1);

print(f'Чек: итоговая стоимость покупки {product_quantity} единиц товара с учетом скидки {discount} % - {total_cost} у.е.')