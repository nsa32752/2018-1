def find_last(filename, key):
    infile = open(filename,"r")
    outfile = open("result.txt","w")
    text = infile.read()
    pos = text.rfind(key)
    if pos == -1:
        outfile.write("not found")
    else:
        outfile.write(str(pos))
    outfile.close()
    infile.close()
    print(pos)

find_last("article.txt","컴퓨터")   # 컴퓨터의 위치번호는 6355
find_last('article.txt','데스크탑') # 데스크탑의 위치번호는 6360
find_last("article.txt","한양대")   # 한양대는 not found