numbers_of_sticks = 10
player_turn = 1

while numbers_of_sticks > 0:
    print(f"How many sticks you take? Remaining {numbers_of_sticks}")
    taken = int(input())

    if taken < 1 or taken > 3:
        print(f'You tried to take {taken}. Allowed to take 1, 2, 3 sticks.')

    numbers_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if numbers_of_sticks <= 0:
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost')

    player_turn = 1 if player_turn == 2 else 2 # перевод стрелок, тип, если остался последний игрок 2, то меняем 1 на 2, если вітягивает 1 игрок, то второй игрок присваеваеться переменной