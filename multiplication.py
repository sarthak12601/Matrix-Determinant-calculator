def multiplication(matrix, row1, col1):

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
        