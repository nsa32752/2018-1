def permutation0(n,k):
    def loop(n,k):
        if k > 0:
            if k == 1:
                return n
            elif n >= k:
                return n * permutation0(n-1, k-1)
            else:
                return 0
        else:
            return 1

    if n > 0:
        return loop(n,k)
    else:
        return 0

def permutation1(n,k):
    def loop(n,k,p):
        if k > 0:
            if k == 1:
                return n * p
            elif n >= k:
                return loop(n-1, k-1, n * p)
            else:
                return 0
        else:
            return 1

    if n > 0:
        return loop(n,k,1)
    else:
        return 0


def permutation(n,k):
    p = 1
    while k > 0:
        if k == 1:
            return n * p
        elif n >= k:
            n, k, p = n-1, k-1, n*p
        else:
            return 0
    else:
        return 1

print(permutation(1,1)) # => 1
print(permutation(2,1)) # => 2
print(permutation(2,2)) # => 2
print(permutation(3,1)) # => 3
print(permutation(3,2)) # => 6
print(permutation(3,3)) # => 6
print(permutation(4,1)) # => 4
print(permutation(4,2)) # => 12
print(permutation(4,3)) # => 24
print(permutation(4,4)) # => 24
