def show_board(board):
    print()
    print('S','|','1','2','3','4')
    print('-','+','-','-','-','-')
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

show_board([[0,3,0,0],[2,4,0,0],[3,1,2,0],[0,2,1,0]])