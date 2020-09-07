def gugudan1():
    blank = ""
    for i in range (2,10):
        if i > 2:
            blank += '\n\n'
        for x in range(2,10):
            if i*x < 10 and x != 5:
                blank += str(i) + ' x ' + str(x) + ' = ' + "".rjust(1) + str(i*x) + ''.rjust(2)
            elif x == 5:
                blank += str(i) + ' x ' + str(x) + ' = ' + str(i*x) + '\n'
            else:
                blank += str(i) + ' x ' + str(x) + ' = ' + str(i*x) + ''.rjust(2)
    return blank

#print(gugudan1())

def gugudan2():
    result1 = ''
    result2 = ''
    for i in range (2,10):
        for x in range(2,10):
            if x == 5:
                if i * x < 10 :
                    result1 += str(x) + 'x' + str(i) + '=' + "".rjust(1) + str(i * x) + ''.rjust(2)
                else:
                    result1 += str(x) + 'x' + str(i) + '=' + str(i * x) + ''.rjust(2)
                result1 += '\n'
            elif x < 5:
                if i * x < 10 :
                    result1 += str(x) + 'x' + str(i) + '=' + "".rjust(1) + str(i * x) + ''.rjust(2)
                else:
                    result1 += str(x) + 'x' + str(i) + '=' + str(i * x) + ''.rjust(2)
            elif x == 9:
                if i * x < 10 :
                    result2 += str(x) + 'x' + str(i) + '=' + "".rjust(1) + str(i * x) + ''.rjust(2)
                else:
                    result2 += str(x) + 'x' + str(i) + '=' + str(i * x) + ''.rjust(2)
                result2 += '\n'
            else:
                if i * x < 10 :
                    result2 += str(x) + 'x' + str(i) + '=' + "".rjust(1) + str(i * x) + ''.rjust(2)
                else:
                    result2 += str(x) + 'x' + str(i) + '=' + str(i * x) + ''.rjust(2)
    return result1 + "\n" + result2

print(gugudan2())

def minsteps(n):
    memo = [0] * (n+1)
    for x in range(n+1):
        if x > 1:
            if memo[x] != 0:
                return memo[x]
            else:
                memo[x] = 1 + memo[x-1]
                if x % 2 == 0:
                    memo[x] = min(memo[x], 1+memo[x//2])
                elif x % 3 == 0:
                    memo[x] = min(memo[x], 1+memo[x//3])
        else:
            memo[x] = 0
    return memo[n]

#print(minsteps(23))


def minsteps1(n):
    memo = [0] * (n + 1)
    def loop(n):
        if n > 1:
            if memo[n] != 0:
                return memo[n]
            else:
                memo[n] = 1 + loop(n - 1)
                if n % 2 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 2))
                if n % 3 == 0:
                    memo[n] = min(memo[n], 1 + loop(n // 3))
                return memo[n]
        else:
            return 0
    return loop(n)


#print(minsteps1(10))


