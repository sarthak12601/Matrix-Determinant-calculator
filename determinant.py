def determinant(matrix, row1, col1):

    if row1==1 and col1==1:
        print(matrix)

    elif row1==2 and col1==2:
        s=matrix[0][0]
        t=matrix[0][1]
        u=matrix[1][0]
        v=matrix[1][1]

        print("Determinant:")
        print((s*v)-(u*t))

    elif row1==3 and col1==3:
        s=matrix[0][0]
        t=matrix[0][1]
        a=matrix[0][2]
        u=matrix[1][0]
        v=matrix[1][1]
        b=matrix[1][2]
        x=matrix[2][0]
        y=matrix[2][1]
        c=matrix[2][2]

        print("Determinant:")
        print((s*((v*c)-(y*b)))-(t*((u*c)-(x*b)))+(a*((u*y)-(x*v))))

    else:
        print("Invalid input")