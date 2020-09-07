def insert0(x,ss):
    if ss != []:
        if x <= ss[0]:
            return [x] + ss
        else:
            return [ss[0]] + insert0(x, ss[1:])
    else:
        return [x]




def insert1(x,ss):
    def loop(ss,left):
        print(ss, left)
        if ss != []:
            if x <= ss[0]:
                return left + [x] + ss
            else:
                return loop(ss[1:],left + [ss[0]])
        else:
            return left + [x]
    return loop(ss,[])






def insert(x,ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            return left + [x] + ss
        else:
            ss, left = ss[1:], left + [ss[0]]
    return left + [x]

print(insert(9,[2,4,5,7,8]))