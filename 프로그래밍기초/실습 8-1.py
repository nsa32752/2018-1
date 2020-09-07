def load_members(): # 아이디를 키로하는 사전
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def store_members(members): # 새로운 사람 입력
    file = open("members.txt","a")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + '\n'
        file.write(line)
    file.close()

def divide(x,y):
    return x/y if y > 0 else 0

def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members:#<members의 키 중에서 username이 있다>:
        if trypasswd == members[username][0]: #<trypasswd가 username의 비밀번호와 일치한다>:
            print("You played " + str(members[username][1]) + " games and won " + str(int(members[username][2])) + " of them.")# username의 게임시도 횟수와 이긴 횟수를 members에서 가져와 보여준다.
            # 예시: You played 101 games and won 54 of them.
            winsper = divide(members[username][2],members[username][1]) * 100
            print("You all-time winning percentage is " + "{0:.1f}".format(winsper) + '%')# 승률 계산하여 %로 보여줌 (분모가 0인 오류 방지해야 함)
            # 예시: Your all-time winning percentage is 53.5 %
            # 칩 보유개수를 보여줌
            if int(members[username][3]) >= 0:
                print("You have "+ str(members[username][3]) + " chips.")
            elif int(members[username][3]) < 0:
                print("You owe " + str(members[username][3]) + " chips.")
            # 예시 : 개수가 양수이면 You have 5 chips.
            # 예시 : 개수가 음수이면 You owe 5 chips.
            return username, members[username][1], members[username][2] , members[username][3], members
        else:
            return login(members)
    else:
        # username을 members 사전에 추가한다.
        members = {username: (trypasswd, 0, 0, 0)}
        store_members(members)
        return username, 0, 0, 0, members


login(load_members())