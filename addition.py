def addition(matrix, row1, col1):

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

        print("Second Matrix:")
        print(*matrix2, sep="\n")

        result = []

        for i in range(row1):
            new_row = []

            for j in range(col1):
                value = matrix[i][j] + matrix2[i][j]
                new_row.append(value)

            result.append(new_row)

        print("Addition:")
        print(*result, sep="\n")

    else:
        print("Invalid input")