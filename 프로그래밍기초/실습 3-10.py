def rsmult1(m,n):
    def loop(m,n,a):
        if n > 1:
            if n % 2 != 0:
                return loop(m*2, n//2, m + a)
            else:
                return loop(m*2, n//2, a)
        else: # n == 1
            return m + a

    if n > 0:
        return loop(m,n,0)
    else:
        return 0

print(rsmult1(57, 86))