def rsmult0(m,n):
    def loop(m,n):
        if n > 1:
            if n % 2 != 0:
                return m + rsmult0(2*m, n//2)
            else:
                return rsmult0(2*m, n//2)
        else: # n == 1
            return m
    if n > 0:
        return loop(m,n)
    else:
        return 0

print(rsmult0(57,86))
