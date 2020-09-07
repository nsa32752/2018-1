def insert(x,ss):
    left = []
    while ss != []:
        if x <= ss[0]:
            return left + [x] + ss
        else:
            ss, left = ss[1:], left + [ss[0]]
    return left + [x]

def isort(s) :
    ss = []
    while s != []:
        s, ss = s[1:], insert(s[0], ss)
    return [] + ss

def isort(s):
    for k in range(1,len(s)):
        for i in range(k, 0, -1):
            if s[i] < s[i-1]:
                s[i], s[i-1] = s[i-1], s[i]a
    return s
