def isinteger(s):
    return s.isdigit() or s[0] == '-' and s[1:].isdigit()

def isfloat(s):
    y = s.partition(".")
    if (y[0] == ''):
        if y[2].isdigit():
            return True
        elif (y[2] == '.'):
            return False
        elif (y[2] == ''):
            return False
    elif (y[0] == '-'):
        if y[2].isdigit():
            return True
    elif isinteger(y[0]):
        if y[2].isdigit():
            return True
        elif (y[2] == ''):
            return True
        else:
            return False
    else:
        return False

x= input()
print(isfloat(x))

