from matrix_input import input_matrix
from transpose import transpose
from determinant import determinant
from addition import addition
from subtraction import subtraction
from multiplication import multiplication

# Code starts 

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

# Input for rows and columns

row1 = int(input("Enter no. of rows in matrix 1: "))

col1 = int(input("Enter no. of columns in matrix 1: "))

matrix = input_matrix(row1, col1)

# Different choices or operations user can perform 

if choice == 4:
    transpose(matrix, row1, col1)

if choice == 5:
    determinant(matrix, row1, col1)

if choice == 1:
    addition(matrix,row1, col1)

if choice == 2:
    subtraction(matrix, row1, col1)

if choice == 3:
    multiplication(matrix, row1, col1)

    