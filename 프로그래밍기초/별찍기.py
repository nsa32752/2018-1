def ascii_art_cross(s):
    for x in range(s):
        for i in range(s):
            if x != s // 2:
                if s//2 == i :
                    print("#",end = '')
                else:
                    print(" ",end = '')
            else:
                print("#", end = '')
        print()


ascii_art_cross(3)

def ascii_art_X(s):
    for x in range(s):
        for i in range(s):
            if (s-1) - x == i or x == i:
                print("#", end = '')
            else:
                print(" ", end='')
        print()

print(ascii_art_X(5))

def ascii_art_square(s):
    for x in range(s):
        for i in range(s):
            if x == 0 or x == s-1:
                print("#", end='')
            else:
                if i == 0 or i == s-1:
                    print("#", end='')
                else:
                    print(" ", end='')
        print()


print(ascii_art_square(5))

def ascii_art_diamond(s):
    for x in range(s):
        for i in range(s):
            if x < s//2:
                if i == (s//2) - x:
                    print("#", end='')
                elif i == (s//2) + x:
                    print("#", end='')
                else:
                    print(" ", end='')
            if x == s//2:
                if i == 0 or i == s-1:
                    print("#", end='')
                else:
                    print(" ", end='')
            if x > s//2:
                if i == (s//2) -(s - x-1):
                    print("#", end='')
                elif i == (s//2) +(s - x-1):
                    print("#", end='')
                else:
                    print(" ", end='')
        print()

print(ascii_art_diamond(5))

def number_art1(s):
    for x in range(s):
        for i in range(s):
            if x >= i:
                print(i + 1, end='')
            else:
                print(" ", end='')
        print()

print(number_art1(5))

def number_art2(s):
    for x in range(s):
        for i in range(s):
            if x <= i:
                print(i+1, end = '')
            else:
                print(" ", end = '')
        print()

print(number_art2(5))

def number_art3(s):
    for x in range(s):
        num = s - x
        for i in range(s):
            if i <= x:
                print(num, end = '')
                num += 1
            else:
                print(" ", end='')
        print()

print(number_art3(5))

def number_art4(s):
    for x in range(s,0,-1):
        for i in range(1,s+1):
            if x >= i:
                print(i, end = '')
            else:
                print(" ", end = '')
        print()

print(number_art4(5))
