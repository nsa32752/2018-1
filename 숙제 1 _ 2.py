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

print(front_ok(991103))