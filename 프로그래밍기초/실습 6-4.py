def transpose(mat):
    no_of_columns = len(mat[0])
    transposed = []
    blank = []
    for m in range(no_of_columns):
        blank = []
        for n in range(len(mat)):
            blank += [mat[n][m]]
            if n == len(mat)-1:
                transposed = transposed + [blank]
    return transposed

def transpose0(mat):
    no_of_columns = len(mat[0])
    size = len(mat)
    transposed = [[]] * no_of_columns
    print(transposed)
    for i in range(no_of_columns):
        for j in range(size):
            transposed[i].append(mat[j][i])
    return transposed

print(transpose0([[1,2,7],[3,4,8],[5,6,9]]))
print(transpose0([[1,2],[3,4]]))