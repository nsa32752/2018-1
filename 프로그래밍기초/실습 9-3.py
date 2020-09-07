class RangeOutInteger(Exception) : pass

def input_float_one():
    while True:
        try :
            n = float(input())
            if not -1.0 <= n <= 1.0: raise RangeOutInteger
        except KeyboardInterrupt:
            break
        except ValueError as e:
            pass
        except RangeOutInteger:
            pass
        else:
            return n

print(input_float_one())