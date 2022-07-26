# a = [(1, 2), (3, 4), (5, 6)]
#
# def duplet(a):
#     a1 = sum(a[0])
#     a2 = sum(a[1])
#     a3 = sum(a[2])
#     if a1 % 2 == 0 or a2 % 2 == 0 or a3 % 2 == 0:
#         print("a == 0")
#     elif a1 % 2 != 0 or a2 % 2 != 0 or a3 % 2 != 0:
#         print(sum(a[0]+a[1]+a[2]))
#     else:
#         print("a")
# duplet(a)

def calc_dice_scores(lst):
    lst1 = lst[0]
    lst2 = lst[1]
    lst3 = lst[2]
    if lst1[0] == lst1[1]:
        return 0
    elif lst2[0] == lst2[1]:
        return 0
    elif lst3[0] == lst3[1]:
        return 0
    else:
        return sum(lst[0]+lst[1]+lst[2])