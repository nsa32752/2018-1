import random
def bin_search_closest(s,key):
    if s == []:
        return None
    len = abs(key-max(s))
    index = 0
    for x in s:
        if abs(key-x) != 0:
            if (abs(key-x) < len):
                len = abs(key-x)
                index = s.index(x)
        elif abs(key-x) == 0:
            len = 0
            index = s.index(x)

    return index

print(bin_search_closest([],3))	#None
print(bin_search_closest([8],3))	#0
print(bin_search_closest([3],3))	#0
print(bin_search_closest([1,2,5,7,8],3))	#1
print(bin_search_closest([1,2,5,7,8],5))	#2
print(bin_search_closest([1,2,5,7,8],6))	#2


def test_bin_search_closest():
    db = random.sample(range(5000000), 1000000)
    db.sort()
    print("Binary search closest function test")
    for _ in range(10):
        key = random.randrange(5000000)
        index = bin_search_closest(db, key)
        print("The closest value to", key, ":", db[index], "at index", index)

test_bin_search_closest()