def bigger(x,y):
    if x > y:
        return x
    else:
        return y

def biggest(x,y,z):
    return bigger(bigger(x,y),z)

def median(x,y,z):
    if (biggest(x,y,z)==x):
      return bigger(y,z)
    elif (biggest(x,y,z)==y):
        return bigger(x,z)
    else:
        return bigger(x,y)

x = int(input())
y = int(input())
z = int(input())
print(median(x,y,z))