# игра в камень ножниці бумага

import random

mode = True
print(type(mode))
while mode:
    user = input("Введите вашу руку - RSP - ")
    hand_ii = random.choice('R' 'S' 'P')
    if user == hand_ii:
        print("User == hand_ii")
    if user == 'R' and hand_ii == 'S':
        print("User win")
    if user == 'R' and hand_ii == 'P':
        print("User foult")
    if user == 'S' and hand_ii == 'P':
        print("User win")
    if user == 'S' and hand_ii == 'R':
        print("User foult")
    if user == 'P' and hand_ii == 'R':
        print("User win")
    if user == 'P' and hand_ii == 'S':
        print("User foult")

    switch = input("Continued?(yes/no)")
    if switch == 'no':
        mode = False
print("Game over")
