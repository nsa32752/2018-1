def issudoku(mat):
    size = len(mat)
    s = []
    for i in range(size):
        for k in range (size):
            if mat[i][k] in s:
                return False
            else:
                s = s + [mat[i][k]]
    return True

m0 =[[1,2],
     [3,4]]
m1 = [[1,7,2],[9,3,4],[5,8,6]]
m2 = [[1,6,2],[9,3,4],[5,8,6]]

print(issudoku(m0))
print(issudoku(m1))
print(issudoku(m2))
