# Matrix Calculator

## Project Title

Matrix Calculator

## Overview

Matrix Calculator is a Python-based project that performs common matrix
operations. The user selects an operation from a menu, enters the
required matrix dimensions and elements, and the program displays the
result.

The current implementation supports matrix input from 1x1 up to 3x3.

## Features

-   Matrix Addition
-   Matrix Subtraction
-   Matrix Multiplication
-   Matrix Transpose
-   Matrix Determinant
-   Exit option

## Functional Requirements

### 1. Addition

Adds two matrices when both matrices have the same number of rows and
columns.

### 2. Subtraction

Subtracts the second matrix from the first matrix when both matrices
have the same dimensions.

### 3. Multiplication

Multiplies two matrices when the number of columns of the first matrix
is equal to the number of rows of the second matrix.

### 4. Transpose

Converts the rows of a matrix into columns and the columns into rows.

### 5. Determinant

Calculates the determinant for 1x1, 2x2 and 3x3 square matrices.

### 6. Exit

Closes the Matrix Calculator.

## Technologies Used

-   Python
-   Python Lists
-   Conditional Statements
-   Loops
-   Functions
-   Modules
-   User Input and Output

## Project Structure

``` text
Matrix Calculator/
│
├── main.py
├── matrix_input.py
├── addition.py
├── subtraction.py
├── multiplication.py
├── transpose.py
├── determinant.py
└── README.md
```

## Module Description

### main.py

Contains the main menu and controls the program.

### matrix_input.py

Takes the rows, columns and elements of the matrix from the user.

### addition.py

Performs matrix addition.

### subtraction.py

Performs matrix subtraction.

### multiplication.py

Performs matrix multiplication and checks whether multiplication is
possible.

### transpose.py

Calculates and displays the transpose of a matrix.

### determinant.py

Calculates and displays the determinant of a square matrix.

## How to Run

1.  Install Python.
2.  Open the project folder in Visual Studio Code.
3.  Open the terminal in the project folder.
4.  Run the following command:

``` bash
python main.py
```

5.  Select an operation from the displayed menu.
6.  Enter the required matrix dimensions and elements.

## Example

For a 2x2 matrix addition:

``` text
Enter your choice: 1
Enter no. of rows in matrix 1: 2
Enter no. of columns in matrix 1: 2

enter a₁₁: 3
enter a₁₂: 4
enter a₂₁: 2
enter a₂₂: 4

Enter the no. of rows in matrix 2: 2
Enter the no. of columns in matrix 2: 2

Enter elements of second matrix:
Enter b11: 1
Enter b12: 2
Enter b21: 3
Enter b22: 4

Addition:
[4, 6]
[5, 8]
```

## Input Validation

The program checks:

-   Matrix dimensions for addition.
-   Matrix dimensions for subtraction.
-   Compatibility of matrices for multiplication.
-   Whether the matrix is suitable for determinant calculation.

If an operation cannot be performed, the program displays an appropriate
message.

## Testing

The project can be tested by:

-   Testing 1x1, 1x2, 1x3, 2x1, 2x2, 2x3, 3x1, 3x2 and 3x3 matrices.
-   Testing addition with matching and non-matching dimensions.
-   Testing subtraction with matching and non-matching dimensions.
-   Testing multiplication with compatible and incompatible matrices.
-   Testing transpose with different matrix dimensions.
-   Testing determinants of 1x1, 2x2 and 3x3 matrices.
-   Testing the Exit option.

## Future Enhancements

-   Support for larger matrix sizes.
-   Matrix inverse.
-   Scalar multiplication.
-   More matrix operations.
-   Better input validation and error handling.
-   Graphical user interface.

## Project Objective

The objective of this project is to apply Python programming concepts by
creating a practical Matrix Calculator. The project uses lists, loops,
conditional statements, functions, user input and modular programming.

## Author

**Sarthak Gandhi**

## License

This project is created as an academic project.

