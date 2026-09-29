def transpose(matrix, row1, col1):
    transpose = []

    for i in range(col1):
        new_row=[]
        for j in range(row1):
            new_row.append(matrix[j][i])
        transpose.append(new_row)

    print("Transpose:")
    print(*transpose,sep="\n")