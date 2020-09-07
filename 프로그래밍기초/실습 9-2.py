def fac(n):
    ans = 1
    while n > 0:
        ans = n * ans
        n = n - 1
    return ans

def factorial():
    while True:
        try:
            n = int(input())
            assert n >= 0
        except ValueError as e:
            pass
        except AssertionError:
            pass
        else:
            print(fac(n))
            break

factorial()