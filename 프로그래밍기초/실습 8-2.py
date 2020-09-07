def load_members(): # 아이디를 키로하는 사전
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(), key=lambda x:x[1][3], reverse=True)# 칩의 개수 역순으로 정렬
    name = []
    for x in range(len(members)):
        name += [sorted_members[x][0]]
    num = []
    for y in range(len(members)):
        num += [sorted_members[y][1][3]]
    print("All-time Top 5 based on the number of chips earned")
    for x in range(len(name)):
        if num[x] != 0:
            print( str(x+1) +". " + name[x] + " : " + str(num[x]))
    # sorted_members[:5]의 원소를 차례대로 참고하여 보여주되 0이하는 무시한다.

show_top5(load_members())