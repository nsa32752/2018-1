def gcd(m,n):
    while n != 0:
          m, n = n, m%n
    return abs(m)

print(gcd(48,18))