def get_level():
    level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    while level not in {"상","중","하"}:
        level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
    if level == "상":
        return 10
    elif level == "중":
        return 8
    elif level == "하":
        return 6

print(get_level())
    # level 이 '하' 이면  return  6
    # level 이 '중' 이면  return  8
    # level 이 '상' 이면  return  10