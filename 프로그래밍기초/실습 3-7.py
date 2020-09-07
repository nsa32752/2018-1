def fastmult1(m, n):
    def loop(m, n, ans):
        if n > 0:
            if n % 2 != 0:
                return loop(m, n-1, m + ans)
            else:
                return loop(m*2, n//2, ans)
        else:
            return ans

    return loop(m, n, 0)


print(fastmult1(3, 6))