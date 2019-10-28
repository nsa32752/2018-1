# #팀플_윷놀이# #팀플_윷놀이
board = [\
    ["◎","   ","○","   ","○","   ","○","   ","○","   ","◎"],\
    [" "," ○ "," ","   ","   ","   ","   ","   ","", " ○ "," "],\
    ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
    [" ","   ","  "," ○ ","  ","   ","  "," ○ ","  ","   "," "],\
    ["○","    "," ","    "," ","   ","  ","   ","  ","   ","○"],\
    [" ","   ","  ","   ","  "," ◎ ","  ","   ","  ","   ","  "],\
    ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
    [" ","   ","  "," ○ ","  ","   ","  "," ○ "," ","   ","  "],\
    ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
    [" "," ○ ","  ","   ","  ","   ","  ","   ","  "," ○ "," "],\
    ["◎","   ","○","   ","○","   ","○","   ","○","   ","◎"]]

def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),int(float(wins)))
    file.close()
    return members

def divide(x,y):
    return x/y if y > 0 else 0

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + '\n'
        file.write(line)
    file.close()

def loginA(members):
    usernameA = input("아이디를 입력하세요 : ")
    while len(usernameA) > 10:
        usernameA = input("아이디를 입력하세요 : ")
    if usernameA in members:
        trypasswd = input("비밀번호를 입력하세요 : ")
        if trypasswd == members[usernameA][0]:
            print("당신은 " + str(members[usernameA][1]) + " 판 중 " + str("{0:.0f}".format(members[usernameA][2])) + " 판의 게임을 승리했습니다" )
            print("당신의 승률은 " + str("{0:.1f}".format(100 * divide(members[usernameA][2], members[usernameA][1])))+ "% 입니다")
            if 0 <= members[usernameA][2] <= 1:
                print("[새내기] " + usernameA + " 님 환영합니다!")
            elif members[usernameA][2] > 1 and members[usernameA][2] <= 5:
                print("[헌내기] " + usernameA + " 님 환영합니다!")
            elif members[usernameA][2] > 5 and members[usernameA][2] <= 20:
                print("[윷놀이 좀 해본 놈인가?] " + usernameA + " 님 환영합니다!")
            elif members[usernameA][2] > 20 and members[usernameA][2] <= 100:
                print("[윷놀이를 잘 아는] " + usernameA + " 님 환영합니다!")
            elif members[usernameA][2] > 100 and members[usernameA][2] <= 500:
                print("[킹 오브 윷놀이] " + usernameA + " 님 환영합니다!")
            elif members[usernameA][2] > 500:
                print("[그만해] " + usernameA + " 님 환영합니다!")
            return usernameA, members[usernameA][0], members[usernameA][1], members[usernameA][2], members
        else:
            return loginA(members)
    else:
        passwdA = input("비밀번호를 입력하세요 : ")
        file = open("members.txt","a")
        file.write(usernameA + ",")
        file.write(passwdA + ",0,0")
        file.write("\n")
        file.close()
        return usernameA, passwdA, 0, 0, members

def loginB(members):
    usernameB = input("아이디를 입력하세요 : ")
    while len(usernameB) > 10:
        usernameB = input("아이디를 입력하세요 : ")
    if usernameB in members: #<members의 키 중에서 username이 있다>:
        trypasswd = input("비밀번호를 입력하세요 : ")
        if trypasswd == members[usernameB][0]: #<trypasswd가 username의 비밀번호와 일치한다>:
            print("당신은 " + str(members[usernameB][1]) + " 판 중 " + str("{0:.0f}".format(members[usernameB][2])) + " 판의 게임을 승리했습니다" )
            print("당신의 승률은 " + str("{0:.1f}".format(100 * divide(members[usernameB][2], members[usernameB][1])))+ "% 입니다")
            if 0 <= members[usernameB][2] <= 1:
                print("[새내기] " + usernameB + " 님 환영합니다!")
            elif members[usernameB][2] > 1 and members[usernameB][2] <= 5:
                print("[헌내기] " + usernameB + " 님 환영합니다!")
            elif members[usernameB][2] > 5 and members[usernameB][2] <= 20:
                print("[윷놀이 좀 해본 놈인가?] " + usernameB + " 님 환영합니다!")
            elif members[usernameB][2] > 20 and members[usernameB][2] <= 100:
                print("[윷놀이를 잘 아는] " + usernameB + " 님 환영합니다!")
            elif members[usernameB][2] > 100 and members[usernameB][2] <= 500:
                print("[킹 오브 윷놀이] " + usernameB + " 님 환영합니다!")
            elif members[usernameB][2] > 500:
                print("[그만해] " + usernameB + " 님 환영합니다!")
            return usernameB, members[usernameB][0], members[usernameB][1], members[usernameB][2], members
        else:
            return loginB(members)
    else:
        passwdB = input("비밀번호를 입력하세요 : ")
        file = open("members.txt","a")
        file.write(usernameB + ",")
        file.write(passwdB + ",0,0")
        file.write("\n")
        file.close()
        return usernameB, passwdB, 0, 0, members

def where(message):
    answer = input(message)
    while not (answer.isdigit() == False and (answer == 'y' or answer =='n')):#(반복 조건):
        answer = input(message)
    return answer == 'y'

def up(num,x,y):
    num = num * 2
    if x - num >= 0:
        return (0, x-num, y)
    elif x - num < 0:
        num = num - x
        return num // 2, 0, 10

def left(num,x,y):
    num = num * 2
    if num-y <= 0:
        if num-y == 0:
            return (0,0,y-num)
        else:
            return (0, 0, y-num)
    elif num-y > 0:
        num = num - y
        return num // 2, 0, 0

def down(num,x,y):
    num = num * 2
    if x + num <= 11:
        return 0,x+num,0
    elif x + num > 11:
        num = num - (10-x)
        return num // 2, 10, 0

def right(num,x,y): # 2, 10, 0
    num = num * 2
    if y + num < 10:
        return 0,10,y+num
    elif y + num >= 10:
        print("해당 말이 완주했습니다!")
    return 0, 20, 20

def set(x,y):
    test1 = "board" + "[" + str(x) + "][" + str(y) + "]"
    small = ['board[0][2]','board[0][4]','board[0][6]','board[0][8]','board[2][0]','board[2][10]','board[4][0]','board[4][10]','board[6][0]','board[6][10]','board[8][0]','board[8][10]','board[10][2]','board[10][4]','board[10][6]','board[10][8]']
    large = ['board[0][0]','board[0][10]','board[10][0]','board[10][10]','board[10][0]','board[10][10]']
    mid1 = ['board[5][5]']
    cross1 = ['board[1][2]','board[9][1]']
    board[10][10] = "◎"
    if test1 in small:
        board[x][y] = "○"
    elif test1 in large:
        board[x][y] = "◎"
    elif test1 in mid1:
        board[x][y] = " ◎ "
    elif test1 in cross1:
        board[x][y] = " ○ "
    else:
        board[x][y] = " ○ "
    # 말 위치값이 10, 10이 아니면 보드판에 모든 말의 위치값을 표시

def cross(num,x,y):
    set(x,y)
    num = num * 2
    if (x == 0 and y == 10) or (x == 0 and y == 0):
        if x == 0 and y == 10:
            num -= 2
            return cross(num//2, 1, 9)
        else:
            num -= 2
            return cross(num//2, 1, 1)
    elif (1<=x<=4 and 6<=y<=9) or (6<=x<=9 and 1<=y<=4):
         if y - num > 0:
             return 0, x+num, y-num
         elif y - num < 0:
             return right((num - y)//2, 10, 0)
         elif y - num == 0:
             return 0, 10, 0
    elif (1<=x<=4 and 1<=y<=4) or (6<=x<=9 and 6<=y<=9):
         if y + num < 10:
            return 0, x+num, y+num
         elif y + num > 10:
             print("해당 말이 완주했습니다!")
             return 0, 20, 20
    elif x == y:
         if where("꺾기? (y/n)"):
             if y + num < 10:
                 return 0, x + num, y + num
             elif y + num > 10:
                 print("해당 말이 완주했습니다!")
                 return 0, 20, 20
         else:
             if y - num > 0:
                 return 0, x - num, y - num
             elif y - num < 0:
                 return right((num - y) // 2, 10, 0)
             elif y - num == 0:
                 return 0, 10, 0

def move(num,x,y,move_num):
    down1 = ['board[0][0]','board[2][0]','board[4][0]','board[6][0]','board[8][0]']
    left1 = ['board[0][2]','board[0][4]','board[0][6]','board[0][8]','board[0][10]']
    right1 = ['board[10][0]','board[10][2]','board[10][4]','board[10][6]','board[10][8]']
    up1 = ['board[2][10]','board[4][10]','board[6][10]','board[8][10]','board[10][10]']
    cross1 = ['board[1][1]','board[2][2]','board[3][3]','board[4][4]','board[5][5]',
              'board[6][6]','board[7][7]','board[8][8]','board[9][9]','board[1][9]',
              'board[3][7]','board[7][3]','board[9][1]']
    test = "board" + "[" + str(x) + "][" + str(y) + "]"
    if x == 0 and y == 10 and move_num == 0 and num > 0:
        if where("꺾기? (y/n)"):
            move_num  += 1
            return cross(num, x, y)
        else:
            move_num += 1
            return left(num, x, y)
    elif x == 0 and y == 0 and move_num == 0 and num > 0:
        if where("꺾기? (y/n)"):
            return cross(num, x, y)
        else:
            return right(num, x, y)
    elif num > 0:
        if test in right1:
            num,x,y = right(num,x,y)
            return num,x,y
        elif test in down1:
            num,x,y = down(num,x,y)
            return num,x,y
        elif test in left1:
            num,x,y = left(num,x,y)
            return num, x, y
        elif test in up1:
            num,x,y = up(num,x,y)
            return num,x,y
        elif test in cross1:
            num,x,y = cross(num,x,y)
            return num,x,y
    elif num < 0:
        if test in down1:
            if x == 0:
                return 0, 0, 2
            else:
                return 0, x-2, 0
        elif test in right1:
            if y == 0:
                if where("꺾기? (y/n)")==True:
                    return 0, 9, 1
                else:
                    return 0, 8, 0
            else:
                return 0, 10, y-2
        elif test in up1:
            if x == 8:
                print("해당 말이 완주했습니다!")
                return 0, 20, 20
            else:
                return 0, x+2, 10
        elif test in left1:
            if y == 10:
                return 0, 2, 10
            else:
                return 0, 0, y+2

        elif test in cross1:
            if y == 5:
                if where("왼쪽으로 꺾기? (y/n)"):
                    return 0, 3, 7
                else:
                    return 0, 3, 3
            elif (1<=x<=4 and 6<=y<=9) or (6<=x<=9 and 1<=y<=4):
                if x==1 and y==9:
                    return 0, 0, 10
                return 0, x-2, y+2
            elif (1<=x<=4 and 1<=y<=4) or (6<=x<=9 and 6<=y<=9):
                if x == 1 and y == 1:
                   return 0, 0, 0
                return 0, x-2, y-2
    return num,x,y

def fin(num,x,y):
    move_num = 0
    while num != 0:
        set(x,y)
        num,x,y = move(num,x,y,move_num)
        move_num += 1
    return x, y

def mal_num_A(A1,mum,x,y):
    if mum == 0:
        return A1
    else:
        A1[mum - 1][0] = x
        A1[mum - 1][1] = y
        return A1

def mal_num_B(B1,mum,x,y):
    if mum == 0:
        return B1
    else:
        B1[mum - 1][0] = x
        B1[mum - 1][1] = y
        return B1

def throw():
    import random
    jipab = [{'도': 1}, {'도': 1}, {'도': 1},{'도': 1},\
         {'개': 2}, {'개': 2},{'개': 2},{'개': 2},{'개': 2},{'개': 2},\
         {'걸' : 3},{'걸' : 3},{'걸' : 3},{'걸' : 3}, \
         {'윷': 4},\
         {'모': 5}, {'빽도': -1}]
    n, k = [], []
    random.shuffle(jipab)
    j = jipab[random.randint(0, 15)]
    while j == {'윷' : 4} or j == {'모': 5}:
          print(list(j.keys())[0] + "!")
          input("한번 더!(엔터를 눌러주세요.)")
          n += list(j.keys())
          k.append(j)
          j = jipab[random.randint(0, 15)]
    print(list(j.keys())[0] + "!")
    k.append(j)
    n += list(j.keys())
    return n, k

def where1(message):
    answer = input(message)
    while not (answer.isdigit() == True and (answer == '1' or answer =='2' or answer =='3' or answer =='4')):#(반복 조건):
        answer = input(message)
    return int(answer)#그냥 answer로 리턴하던 것에 int를 씌웠다.

def origin_board():#깨끗한 놀이판, show_board에서만 사용한다.
    return [\
    ["◎","   ","○","   ","○","   ","○","   ","○","   ","◎"],\
    [" "," ○ "," ","   ","   ","   ","   ","   ","", " ○ "," "],\
    ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
    [" ","   ","  "," ○ ","  ","   ","  "," ○ ","  ","   "," "],\
    ["○","    "," ","    "," ","   ","  ","   ","  ","   ","○"],\
    [" ","   ","  ","   ","  "," ◎ ","  ","   ","  ","   ","  "],\
    ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
    [" ","   ","  "," ○ ","  ","   ","  "," ○ "," ","   ","  "],\
    ["○","   ","  ","   ","  ","   ","  ","   ","  ","   ","○"],\
    [" "," ○ ","  ","   ","  ","   ","  ","   ","  "," ○ "," "],\
    ["◎","   ","○","   ","○","   ","○","   ","○","   ","◎"]]



def show_board(A1, B1, X, Y):
    board = origin_board()#깨끗한 놀이판
    mum = 0
    for i in A1:#A팀의 말 입력
        if i != [10,10] and i != [20,20]:
            board[i[0]][i[1]] = X[mum]
        mum += 1
    mum = 0
    for i in B1:#B팀의 말 입력
        if i != [10,10] and i != [20,20]:
            board[i[0]][i[1]] = Y[mum]
        mum += 1
    for row in board:
        for x in range(11):
            print(row[x], end='')
        print()

def same_pos_A(mum,A1,B1):
    for i in range(4):
        if (mum-1 != i) and (A1[mum-1] == A1[i]) and (A1[mum-1] != [10,10]) and (A1[mum-1] != [20,20]):
           return 1 #아군의 말과 같은 위치일 때
        elif (A1[mum-1] == B1[i]) and (B1[i] != [10,10]) and (B1[i] != [20,20]):
             B1[i] = [10,10]
             return 0
    return 2

def same_pos_B(mum,A1,B1):
    for i in range(4):
        if (mum-1 != i) and (B1[mum-1] == B1[i]) and (B1[mum-1] != [10,10]) and (B1[mum-1] != [20,20]):
           return 1
        elif B1[mum-1] == A1[i] and (A1[i] != [10,10]) and (A1[i] != [20,20]):
             A1[i] = [10,10]
             return 0
    return 2

def mal_E_up_seong(X):
    count = 0
    for a in X:
        if a in [[10,10],[20,20]]:
           count += 1
    if count == 4:
       return True
    else:
        return False

def main_game():
    print("Contradiction 윷놀이에 오신 것을 환영합니다!")
    usernameA, passwdA, triesA, winsA, members = loginA(load_members())
    usernameB, passwdB, triesB, winsB, members = loginB(load_members())
    Games = 1
    X = ["❶", "❷", "❸", "❹"]
    Y = ["➀", "➁", "➂", "➃"]
    A1 = [[10, 10], [10, 10], [10, 10], [10, 10]]
    B1 = [[10, 10], [10, 10], [10, 10], [10, 10]]
    n, k = [],[]
    while True:
          input("A팀의 턴입니다!\n엔터키를 눌러 윷을 던져주세요.")
          n1, k1 = throw()
          n += n1
          k += k1
          while n != []:
                if n == ['빽도'] and mal_E_up_seong(A1):
                   print("이런! 움직일 수 있는 말이 없네요. 턴이 넘어갑니다.")
                   n,k = [],[]#빽도 치워주기
                   break
                if len(n)>1:#윷을 여러번 던졌을 때
                   print(n)
                   z = input("어느 것으로 먼저 움직이시겠습니까?")
                   while not ((z == "도") or (z == "개") or (z == "걸") or (z == "윷") or (z == "모") or (z == "빽도")):
                         if z not in n:#한글이 맞지만 뽑은 것이 아닐 경우
                            z = input("제대로 선택해 주십시오.")
                         else:#뭣도 아닐 경우
                             z = input("제대로 선택해 주십시오")
                else:#한번만 뽑았을 때
                    z = n[0]
                mum = where1("몇번 말을 움직이시겠습니까?")
                while z == '빽도' and A1[mum-1] == [10,10]:
                      mum = where1("해당 말은 빽도로 움직일 수 없는 위치에 있습니다.\n다른 말을 선택해 주세요.")
                while A1[mum-1] == [20,20]:#이미 완주한 말을 움직이려 할 때
                      mum = int(input("해당 말은 이미 완주했습니다.\n다른 말을 선택해 주세요."))
                x1, y1 = A1[mum - 1][0], A1[mum - 1][1]#움직이려는 말의 위치정보
                x, y = fin(k[n.index(z)][z],x1,y1)#움직였을 때의 위치정보
                A1 = mal_num_A(A1, mum, x, y)
                p = same_pos_A(mum,A1,B1)#p는 0에서2중에 하나의 정수
                while p == 1 or p == 0:
                      if p == 1:
                         x, y = fin(1,A1[mum-1][0],A1[mum-1][1])
                         A1 = mal_num_A(A1, mum, x, y)
                         print('점프!')
                         p = same_pos_A(mum,A1,B1)
                      elif p == 0:
                           show_board(A1, B1, X, Y)
                           print("상대의 말을 잡았습니다!")
                           input("한번 더 윷을 던질 수 있습니다. 엔터를 눌러주세요.")
                           n1, k1 = throw()#추가던지기
                           n += n1
                           k += k1
                           p = same_pos_A(mum,A1,B1)
                show_board(A1, B1, X, Y)
                k.remove(k[n.index(z)])
                n.remove(z)
                if A1 == [[20,20],[20,20],[20,20],[20,20]]:#승리조건
                    WA, WB = 1, 0
                    members[usernameA] = (passwdA, triesA + Games, winsA + WA)
                    members[usernameB] = (passwdB, triesB + Games, winsB + WB)
                    store_members(members)
                    return print("A팀의 승리입니다!")
          input("B팀의 턴입니다!\n엔터키를 눌러 윷을 던져주세요.")
          n1, k1 = throw()
          n += n1
          k += k1
          while n != []:
                if n == ['빽도'] and mal_E_up_seong(B1):
                   print("이런! 움직일 수 있는 말이 없네요. 턴이 넘어갑니다.")
                   n, k = [], []
                   break
                if len(n)>1:
                   print(n)
                   z = input("어느 것으로 먼저 움직이시겠습니까?")
                   while not ((z == "도") or (z == "개") or (z == "걸") or (z == "윷") or (z == "모") or (z == "빽도")):
                         if z not in n:
                            z = input("제대로 선택해 주십시오.")
                         else:
                             z = input("제대로 선택해 주십시오")
                else:
                    z = n[0]
                mum = where1("몇번 말을 움직이시겠습니까?")
                while (z == '빽도' and B1[mum-1] == [10,10]):
                      mum = where1("해당 말은 빽도로 움직일 수 없는 위치에 있습니다.\n다른 말을 선택해 주세요.")
                while B1[mum - 1] == [20, 20]:
                    mum = int(input("해당 말은 이미 완주했습니다.\n다른 말을 선택해 주세요."))
                x1, y1 = B1[mum - 1][0], B1[mum - 1][1]
                x, y = fin(k[n.index(z)][z], x1, y1)
                B1 = mal_num_B(B1, mum, x, y)
                p = same_pos_B(mum, A1, B1)
                while p == 1 or p == 0:
                      if p == 1:
                         x, y = fin(1, B1[mum-1][0], B1[mum-1][1])
                         B1 = mal_num_B(B1, mum, x, y)
                         print('점프!')
                         p = same_pos_B(mum, A1, B1)
                      elif p == 0:
                           show_board(A1, B1, X, Y)
                           print("상대의 말을 잡았습니다!")
                           input("한번 더 윷을 던질 수 있습니다. 엔터를 눌러주세요.")
                           n1, k1 = throw()
                           n += n1
                           k += k1
                           p = same_pos_B(mum, A1, B1)
                show_board(A1, B1, X, Y)
                k.remove(k[n.index(z)])
                n.remove(z)
                if B1 == [[20, 20], [20, 20], [20, 20], [20, 20]]:
                    WA, WB = 0, 1
                    members[usernameA] = (passwdA, triesA + Games, winsA + WA)
                    members[usernameB] = (passwdB, triesB + Games, winsB + WB)
                    store_members(members)
                    return print("B팀의 승리입니다!")

main_game()
# throw()
# show_board()
