# Написать игру "Камень, ножницы, бумага". Компьютер случайным образом выбирает один из
# вариантов. Пользователь

import random

rounds = 1; # номер раунда
game_list = ['камень', 'ножницы', 'бумага'];


def rock_scissors_paper(rounds:int):
    while(True):
        # Количество выигрышей
        pc_wins = 0; # компьютера
        user_wins = 0; # пользователя
        
        pc_try = random.sample(game_list,1); # выбор варианта компьютером
        user_try = [];
        user_try.append(input('Введите свой вариант: '));
        
        if(pc_try == user_try):
            print(f'Раунд {rounds} в ничью');
            rounds += 1;
            continue;
        elif(((pc_try == 'камень') and (user_try == 'ножницы')) or ((pc_try == 'ножницы') and (user_try == 'бумага')) or ((pc_try == 'бумага') and (user_try == 'камень'))):
            print(f'Раунд {rounds} за компьютером!');
            pc_wins += 1;
            rounds += 1;
        elif((user_try == 'камень' and pc_try == 'ножницы') or (user_try == 'ножницы' and pc_try == 'бумага') or (user_try == 'бумага' and pc_try == 'камень')):
            print(f'Раунд {rounds} за вами!');
            user_wins += 1;
            rounds += 1;
        
        if(user_wins == 3):
            print('Вы выиграли!');
            break;
        elif(pc_wins == 3):
            print('Выиграл компьютер!');
            break;

rock_scissors_paper(rounds);