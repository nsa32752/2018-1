def one_sentence_per_line(filename):
    infile = open('C:/Users/nsa32/PycharmProjects/untitled/article.txt', "r")
    outfile = open("result5.txt", "w")
    text = infile.read()
    count = 0
    print(count)
    while text != "":
        line = text.partition(".")
        if line[2] != []:
            print(count)
            count = count +1
            outfile.write(line[0])
            outfile.write(line[1])
            outfile.write("\n")
            blank= text.partition("."or"?")[2]
            text = blank[1:]
    print(count)
    outfile.write("문장이 총 " + str(count) + "개\n")
    outfile.close()
    infile.close()
    print("done")

one_sentence_per_line("article.txt")   # 총 12번 등장
