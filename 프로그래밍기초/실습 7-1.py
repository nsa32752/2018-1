import random
def create_board():
    seed = [1,2,3,4]
    random.shuffle(seed)
    print(seed)
    base = []
    num = seed
    for x in range(0,len(seed)):
        if x == 0:
            base += [num]
        if x != 0 and x % 2 == 0:
            num = [num[len(seed)-1]] + num[len(seed)//2: len(seed)-1] + [num[len(seed)//2-1]] + num[0:len(seed)//2-1]
            base += [num]
            print(num)
        if x % 2 != 0:
            num = num[len(seed)//2:]+num[0:len(seed)//2]
            base += [num]
            print(num)
    return base


print(create_board())