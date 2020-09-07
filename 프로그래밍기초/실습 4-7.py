def merge1(left,right):
    def loop(left,right,ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                return loop(left[1:], right, ss)
            else:
                ss.append(right[0])
                return loop(left, right[1:], ss)
        else:
            return ss + left + right
    return loop(left,right,[])

def merge(left,right):
    ss = []
    while not (left == [] or right == []):
        if left[0] <= right[0]:
            ss.append(left[0])
            left, right, ss = left[1:], right, ss
        else:
            ss.append(right[0])
            left, right, ss = left, right[1:], ss
    return ss + left + right

print(merge([18,23,32],[7,11,55,99]))