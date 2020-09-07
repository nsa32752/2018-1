def find_all_sentence(filename,key) :
    infile = open('C:/Users/nsa32/PycharmProjects/untitled/article2.txt',"r")
    outfile = open("result0.txt","w")
    text = infile.read()
    count_word = 0
    count_line = 0

    while (len(text) > 0):
        if text.find(".") < text.find("?"):
            line = text.partition(".")
            if line[0].find(key) > 0:
                count_line += 1
                count_word += line[0].count(key)
                outfile.write(""+str(key)+"이(가)"+str(line[0].count(key)) + "번 등장\n")
                outfile.write(line[0].strip() +line[1]+'\n')
            text = text.partition(".")[2]

        elif  text.find(".") > text.find("?") and text.find("?") != -1:
            line = text.partition("?")
            if line[0].find(key) > 0:
                count_line += 1
                count_word += line[0].count(key)
                outfile.write("" + str(key) + "이(가)" + str(line[0].count(key)) + "번 등장\n")
                outfile.write(line[0].strip() + line[1]+"\n")
            text = text.partition("?")[2]

        elif text.find(".") != -1 and text.find("?") == -1:
            line = text.partition(".")
            if line[0].find(key) > 0:
                count_line += 1
                count_word += line[0].count(key)
                outfile.write("" + str(key) + "이(가)" + str(line[0].count(key)) + "번 등장\n")
                outfile.write(line[0].strip() + line[1]+"\n")
            text = text.partition(".")[2]

        elif text.find(".") == -1 and text.find("?") == -1:
            break

    outfile.write(str(key) + "이(가)" + str(count_line) + "개 문장에서 " + str(count_word) + "번 등장\n")
    outfile.close()
    infile.close()
    print("done")

find_all_sentence("article.txt","컴퓨터")