matrix = [[1,2,3,0], [4,5,6,1],[7,8,9,0]]
mat = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        mat.append(matrix[j][i])
    print(mat)
    mat = []

    