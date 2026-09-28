print("=========================")
print("|   Matrix Calculator   |")
print("=========================")
print("| 1. Addition           |")
print("| 2. Subtraction        |")
print("| 3. Multiplication     |")
print("| 4. Transpose          |")
print("| 5. Determinant        |")
print("| 6. Exit               |")
print("|_______________________|")
 
choice=int(input("Enter your choice: "))

if choice == 6:
    print("Exiting Matrix Calculator...")
    exit()

row1 = int(input("Enter no. of rows in matrix 1: "))
col1 = int(input("Enter no. of columns in matrix 1: "))

if row1==1 and col1==1:
    p= int(input("enter a\u2081\u2081:"))
    matrix = [[p]]
    print(matrix)
elif row1==1 and col1==2:
    q=int(input("enter a\u2081\u2081:"))
    r=int(input("enter a\u2081\u2082:"))
    matrix=[[q,r]]
    print(matrix)

elif row1==1 and col1==3:
    s=int(input("enter a\u2081\u2081:"))
    t=int(input("enter a\u2081\u2082:"))
    u=int(input("enter a\u2081\u2083:"))
    matrix=[[s,t,u]]
    print(matrix)

elif row1==2 and col1==1:
    s=int(input("enter a\u2081\u2081:"))
    t=int(input("enter a\u2082\u2081:"))
    matrix=[[s],[t]]
    print(*matrix,sep="\n")

elif row1==3 and col1==1:
    s=int(input("enter a\u2081\u2081:"))
    t=int(input("enter a\u2082\u2081:"))
    u=int(input("enter a\u2083\u2081:"))
    matrix=[[s],[t],[u]]
    print(*matrix,sep="\n")

elif row1==2 and col1==2:
    s=int(input("enter a\u2081\u2081:"))
    t=int(input("enter a\u2081\u2082:"))
    u=int(input("enter a\u2082\u2081:"))
    v=int(input("enter a\u2082\u2082:"))
    matrix=[
        [s,t],
        [u,v]
    ]
    print(*matrix,sep="\n")

elif row1==2 and col1==3:
    s=int(input("enter a\u2081\u2081:"))
    t=int(input("enter a\u2081\u2082:"))
    u=int(input("enter a\u2081\u2083:"))
    v=int(input("enter a\u2082\u2081:"))
    x=int(input("enter a\u2082\u2082:"))
    y=int(input("enter a\u2082\u2083:"))    
    matrix=[
        [s,t,u],
        [v,x,y]
    ]
    print(*matrix,sep="\n")

elif row1==3 and col1==2:
    s=int(input("enter a\u2081\u2081:"))
    t=int(input("enter a\u2081\u2082:"))
    u=int(input("enter a\u2082\u2081:"))
    v=int(input("enter a\u2082\u2082:"))
    x=int(input("enter a\u2083\u2081:"))
    y=int(input("enter a\u2083\u2082:"))    
    matrix=[
        [s,t],
        [u,v],
        [x,y]
        
    ]
    print(*matrix,sep="\n")

elif row1==3 and col1==3:
    s=int(input("enter a\u2081\u2081:"))
    t=int(input("enter a\u2081\u2082:"))
    a=int(input("enter a\u2081\u2083:"))
    u=int(input("enter a\u2082\u2081:"))
    v=int(input("enter a\u2082\u2082:"))
    b=int(input("enter a\u2082\u2083:"))
    x=int(input("enter a\u2083\u2081:"))
    y=int(input("enter a\u2083\u2082:"))
    c=int(input("enter a\u2083\u2083:"))    
    matrix=[
        [s,t,a],
        [u,v,b],
        [x,y,c]
        
    ]
    print(*matrix,sep="\n")


if choice == 4:
    transpose = []
    for i in range(col1):
        new_row=[]
        for j in range(row1):
            new_row.append(matrix[j][i])
        transpose.append(new_row)    
    print("Transpose:")
    print(*transpose,sep="\n")

if choice==5:
    if row1==1 and col1==1:
        print(matrix)
    elif row1==2 and col1==2:
        print("Determinant:")
        print((s*v)-(u*t))
    elif row1==3 and col1==3:
        print("Determinant:")
        print((s*((v*c)-(y*b)))-(t*((u*c)-(x*b)))+(a*((u*y)-(x*v))))
    else:
        print("Invalid input")

if choice==1:
    row2=int(input("Enter the no. of rows in matrix 2: "))
    col2=int(input("Enter the no. of columns in matrix 2: ")) 

    if row2==row1 and col2==col1:

     matrix2 = []

     print("Enter elements of second matrix:")

     for i in range(row2):
        new_row = []

        for j in range(col2):
            value = int(input(f"Enter b{i+1}{j+1}: "))
            new_row.append(value)

        matrix2.append(new_row)

        print(*matrix2, sep="\n")



    
        result = []

        for i in range(row2):
         new_row = []

         for j in range(col2):
            value = matrix[i][j] + matrix2[i][j]
            new_row.append(value)

         result.append(new_row)

        print("Addition:")
        print(*result, sep="\n")
    else:
        print("Invalid input")


if choice == 2:
    row2=int(input("Enter the no. of rows in matrix 2: "))
    col2=int(input("Enter the no. of columns in matrix 2: ")) 
    if row2==row1 and col2==col1:

     matrix2 = []

    print("Enter elements of second matrix:")

    for i in range(row2):
        new_row = []

        for j in range(col2):
            value = int(input(f"Enter b{i+1}{j+1}: "))
            new_row.append(value)

        matrix2.append(new_row)

    print(*matrix2, sep="\n")


   
    result = []

    for i in range(row2):
        new_row = []

        for j in range(col2):
            value = matrix[i][j] - matrix2[i][j]
            new_row.append(value)

        result.append(new_row)

    print("Subtraction:")
    print(*result, sep="\n")

if choice==3:
   
    row2 = int(input("Enter no. of rows of matrix 2: "))
    col2 = int(input("Enter no. of columns of matrix 2: "))

    
    if col1 != row2:
        print("Multiplication is not possible.")
        print("Number of columns of first matrix must be equal to number of rows of second matrix.")

    else:
        matrix2 = []

        print("Enter elements of second matrix:")

        for i in range(row2):
            new_row = []

            for j in range(col2):
                value = int(input(f"Enter b{i+1}{j+1}: "))
                new_row.append(value)

            matrix2.append(new_row)

        print(*matrix2, sep="\n")

       
        result = []

        for i in range(row1):
            new_row = []

            for j in range(col2):
                total = 0

                for k in range(col1):
                    total = total + matrix[i][k] * matrix2[k][j]

                new_row.append(total)

            result.append(new_row)

        print("Multiplication:")
        print(*result, sep="\n")