square = ([
    [1, 3, 2],
    [9, 6, 8],
    [4, 5, 6]
])

def any_duplicates(square):
    y = square[0] + square[1] + square[2]
    x = 0
    x = list(range(1, 10))
    print(x)

    b = sorted(y)
    print(y)
    if x == b:
        print(True)
    else:
        print(False)




#     return any(a==b==c for a, b, c in sudoku_1)
any_duplicates(square)