def isleapyear(year):
    if year >= 0:
        if 0 < year%4 < 4:
            return False
        if year%4 < 1:
            if year % 400 < 1:
                return True
            elif year % 100 < 1:
                return False
            else:
                return True
    else:
        return None

year = int(input())
print(isleapyear(year))