def find_all(filename, key):
    infile = open('C:/Users/nsa32/PycharmProjects/untitled/article.txt',"r")
    outfile = open("result.txt","w")
    text = infile.read()
    pos = 0
    num = 0

    num = text.count(key)

    if num == 0:
        outfile.write("not found")
        print("not found")
    else:
        while text.find(key,pos) != -1:
                pos = text.find(key, pos)
                outfile.write(str(pos)+"\n")
                print(pos)
                pos = pos +1


    outfile.close()
    infile.close()


find_all("article.txt","컴퓨터")   # 총 12번 등장
find_all("article.txt","데스크탑") # 총 1번 등장
find_all("article.txt","한양대")   # 없음
