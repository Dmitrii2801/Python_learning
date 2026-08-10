# Применение условного оператора (условия с логическим типом данных)

is_sunny = bool(int(input('На улице солнечно? (1/0) ')));
is_weekend = bool(int(input('У вас сегодня выходной? (1/0) ')));

print(is_sunny)
print(is_weekend)

# Обработка условия для логических типов данных
if(is_sunny and is_weekend):
    print('Идеальный день для прогулки');
elif(is_sunny and not is_weekend):
    print('Погода хорошая, но нужно поработать');
elif(not is_sunny and is_weekend):
    print('Можно остаться дома и отдохнуть');
else:
    print('Рабочий день с плохой погодой');
