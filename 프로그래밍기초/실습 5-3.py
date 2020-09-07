def find_all(filename, key):
    infile = open('C:/Users/nsa32/PycharmProjects/untitled/article.txt', "r")
    outfile = open("result1.txt", "w")
    text = infile.read()
    pos = 0
    num = 0

    num = text.count(key)

    if num == 0:
        outfile.write("not found")

    else:
        while text.find(key, pos) != -1:
            pos = text.find(key, pos)
            outfile.write(str(pos) + " ")
            pos = pos + 1

    num = text.count(key)
    outfile.write(str(num))
    print(num)
    outfile.close()
    infile.close()

find_all("article.txt","컴퓨터")   # 총 12번 등장
find_all("article.txt","데스크탑") # 총 1번 등장
find_all("article.txt","한양대")   # 없음
