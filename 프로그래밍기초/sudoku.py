import random
def create_board():
    seed = [1,2,3,4,5,6]
    random.shuffle(seed)
    base = []
    num = seed
    for x in range(0,len(seed)):
        if x == 0:
            base += [num]
        if x != 0 and x % 2 == 0:
            num = [num[len(seed)-1]] + num[len(seed)//2: len(seed)-1] + [num[len(seed)//2-1]] + num[0:len(seed)//2-1]
            base += [num]
        if x % 2 != 0:
            num = num[len(seed)//2:]+num[0:len(seed)//2]
            base += [num]
    return base

def transpose(board): #세로줄 바꾸기
    for i in range(len(board)):
        for x in range(len(board)):
            if 0 <= x < len(board)//2-1:
                board[i][x], board[i][x+1] = board[i][x+1], board[i][x]
            elif len(board)//2 <= x < len(board)-1:
                board[i][x], board[i][x + 1] = board[i][x + 1], board[i][x]
    return board

def trans(board):
    for i in range(len(board)):
        for x in range(len(board)):
            if x == 0:
                board[i][x], board[i][len(board)//2 - 1] = board[i][len(board)//2-1], board[i][x]
            elif x == len(board)//2:
                board[i][x], board[i][len(board)-1] = board[i][len(board)-1], board[i][x]
    return board

def shuffle_ribbons(board):
    shuffle = []
    for x in range(0,len(board)):
        if x!= len(board)-1 and x % 2 == 0:
            shuffle += [board[x+1]]
        elif x!=len(board)-1 and x % 2 == 1:
            shuffle += [board[x-1]]
        elif x == len(board)-1:
            shuffle += [board[x-1]]
    return shuffle

def create_solution_board(board):
    solve = transpose(board)
    solve1 = shuffle_ribbons(solve)
    solve2 = trans(solve1)
    return solve2

def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if level == "상":
        return 17
    elif level == "중":
        return 15
    elif level == "하":
        return 13

def copy_board(board):
    board_clone = []
    for row in board :
        row_clone = row[:]
        board_clone.append(row_clone)
    return board_clone

def make_holes(board,no_of_holes):
    holeset = set()
    import random
    while no_of_holes > 0:
        i = random.randint(1,6) -1
        j = random.randint(1,6) -1
        if board[i][j] != 0:
            board[i][j] = 0
            holeset.add((i,j))
            no_of_holes -= 1
    return (board, holeset)

def show_board(board):
    print()
    print('S','|','1','2','3','4','5','6')
    print('-','+','-','-','-','-','-','-')
    i = 1
    for row in board:
        if i != 1:
            print("")
        print(i,'|', end = "")
        i += 1
        line = ''
        for x in range(len(row)):
            if row[x] == 0:
                print(" .", end = '')
            else:
                print("",row[x], end = '')
    print()

def get_integer(message,i,j):
    number = input(message)
    while not (number.isdigit() and i <= int(number) <= j):
        number = input(message)
    return int(number)

def sudok6x6():
    board = create_board()
    solution = create_solution_board(board)
    no_of_holes = get_level()
    puzzle = copy_board(solution)
    (puzzle,holeset) = make_holes(puzzle,no_of_holes)
    show_board(puzzle)
    while no_of_holes > 0:
        i = get_integer("가로줄번호(1~6): ",1,6) - 1
        j = get_integer("세로줄번호(1~6): ",1,6) - 1
        if (i,j) not in holeset:
            print("빈칸이 아닙니다.")
            continue
        n = get_integer("숫자(1~6): ",1,6)
        sol = solution[i][j]
        if n == sol:
            puzzle[i][j] = sol
            show_board(puzzle)
            holeset.remove((i,j))
            no_of_holes -= 1
        else:
            print(n,"가 아닙니다. 다시 해보세요.")
    print("잘 하셨습니다. 또 들려주세요.")

sudok6x6()