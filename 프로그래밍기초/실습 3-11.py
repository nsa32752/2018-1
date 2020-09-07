def rsmult(m,n):
    a = 0
    while n > 1:
        if n % 2 != 0:
           m, n, a = m*2, n//2, m + a
        else:
            m, n, a = m * 2, n // 2, a
    return m + a

print(rsmult(57, 86))