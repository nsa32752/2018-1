def insert(x,ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            return left + [x] + ss
        else:
            ss, left = ss[1:], left + [ss[0]]
    return left + [x]

def isort1(s):
    def loop(s,ss):
        print(s,ss)
        if s != []:
            return loop(s[1:], insert(s[0],ss))
        else:
            return [] + ss
    return loop(s,[])
