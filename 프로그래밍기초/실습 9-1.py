def input_float():
    while True:
        try:
            s= input()
            k = float(s)
        except ValueError as k:
            pass
        else:
            return s

print(input_float())