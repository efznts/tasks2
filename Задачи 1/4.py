import random

player_move = input('Сделайте ваш ход ("камень", "ножницы" или "бумага"): ').lower()

moves = ['камень', 'ножницы', 'бумага']
computer_move = random.choice(moves)

if player_move != 'камень' and player_move != 'ножницы' and player_move != 'бумага':
    print('Такого хода нет')
else:
    if player_move == computer_move:
        print('Ничья')
    elif (player_move == "камень" and computer_move == "ножницы") or (player_move == "ножницы" and computer_move == "бумага") or (player_move == "бумага" and computer_move == "камень"):
        print('Вы победили')
    else:
        print('Вы проиграли')
