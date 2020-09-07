def fastmult(m,n):
    ans = 0
    while n > 0:
        if n % 2 != 0:
           ans = m + ans
           n = n - 1
        else:
           m, n, ans = m*2, n//2, ans
    return ans


print(fastmult(3,6))