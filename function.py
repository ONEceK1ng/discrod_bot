
# def solve_hanoi_tower(discs, pin1, pin2):
#     if discs == 1:
#         print(f'Perelagili disk 1 so stergnia {pin1} na {pin2}')
#     else:
#         solve_hanoi_tower(discs - 1, pin1, 6 - pin1 - pin2)
#         print(f'Perelagili disk {discs} so stergnia {pin1} na {pin2}')
#         solve_hanoi_tower(discs - 1, 6 - pin1 - pin2, pin2)

def hanoi(discs):
    return 2**discs - 1
print(hanoi(5))