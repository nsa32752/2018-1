def make_holes(board,no_of_holes):
    holeset = set()
    import random
    while no_of_holes > 0:
        i = random.randint(1,4) -1
        j = random.randint(1,4) -1
        if board[i][j] != 0:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes -= 1
    return (board, holeset)

board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(make_holes(board,8))