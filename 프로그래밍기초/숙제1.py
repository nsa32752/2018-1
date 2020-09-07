def front_ok(front):
    year = int(front[0]) * 10 + int(front[1])
    month = int(front[2]) * 10 + int(front[3])
    date = int(front[4]) * 10 + int(front[5])

    if year >= 20:
        year = year + 1900
    else:
        year = year + 2000

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return date <= 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return date <= 30
    else:
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            return date <= 29
        else:
            return date <= 28

def back_ok(s):

    check = 11 - ((2*int(s[0]) + 3*int(s[1]) + 4*int(s[2]) + 5*int(s[3]) + 6*int(s[4]) + 7*int(s[5]) + 8*int(s[7]) + 9*int(s[8]) + 2*int(s[9]) + 3*int(s[10]) + 4*int(s[11]) + 5*int(s[12])) % 11)
    check = check % 10
    if int(s[13]) == check:
        return True
    else:
        return False

def isRRN(s):
    (front, mid, back) = s.partition("-")
    return front_ok(front) and mid == "-" and back_ok(s)

s=input()
print(isRRN(s))