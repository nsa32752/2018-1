def fastmult0(m,n):
    if n > 0:
        if n % 2 == 0:
            return (2*m)*(n//2)
        else:
            return n + fastmult0(n, m-1)
    else:
        return 0

print(fastmult0(3,6))