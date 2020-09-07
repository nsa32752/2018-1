def comb_pascal(n, r):
    matrix = [[]] * (n - r + 1)
    matrix[0] = [1] * (r + 1)
    for i in range(1, n - r + 1):
        matrix[i] = [1]
    for i in range(1, n - r + 1):
        for j in range(1, r + 1):
            newvalue = matrix[i][j - 1] + matrix[i - 1][j]
            matrix[i].append(newvalue)
    return matrix[n - r][r]

class RangeOutInteger(Exception) : pass

def combination():
    while True:
        try:
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            if not 0 < r <= n: raise RangeOutInteger
        except ValueError as e:
            pass
        except KeyboardInterrupt:
            print("Goodbye!")
            break
        except RangeOutInteger:
            pass
        else:
            print(str(n)+"C"+str(r)," = ",comb_pascal(n,r))


print(combination())