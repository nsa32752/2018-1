def bsort(s):
    print(len(s))
    for k in range(len(s)-1):
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                s[i], s[i+1] = s[i+1], s[i]
    return s


print(bsort([32,23,18,7,11,99,55]))