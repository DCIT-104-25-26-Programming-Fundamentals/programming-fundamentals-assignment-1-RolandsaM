# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows,cols):
    matrix=[]
    for i in range(rows):
        row_input = input("Enter row " + str(i + 1) + ": ")
        row = [int(x) for x in row_input.split()]
        matrix.append(row)
    return matrix

def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="\t")
        print()

def transpose(matrix,rows,cols):
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result

def add_matrices(a, b, rows, cols):
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(a[i][j] + b[i][j])
        result.append(new_row)
    return result

def multiply_matrices(a, b, m, n, p):
    result = []
    for i in range(m):
        new_row = []
        for j in range(p):
            total = 0
            for k in range(n):
                total = total + a[i][k] + b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result

print("PART A: Transpose")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = read_matrix(rows, cols)
print("Original matrix:") 
display_matrix(matrix)
print("Transposed Matrix:")
display_matrix(transpose(matrix, rows, cols))

print()
print("PART B: Add Two Matrices")
rows2 = int(input("Enter number of rows: "))
cols2 = int(input("Enter number of colums: "))
print("Matrix A:")
matrix_a = read_matrix(rows2, cols2)
print("Matrix B:")
matrix_b = read_matrix(rows2, cols2)
print("Sum:")
display_matrix(add_matrices(matrix_a,matrix_b, rows2, cols2))

print()
print("PART C: Multiply Two Matrices")
m = int(input("Enter rows of matrix A: "))
n = int(input("Enter columns of matrice A / rows of matrix B: "))
p = int(input("Enter colums of matrix B: "))
print("Matrix A:")
matrix_a2 = read_matrix(m, n)
print("Matrix B:")
matrix_b2 = read_matrix(n, p)
print("Product:")
display_matrix("multipy_matrices"(matrix_a2, matrix_b2, m, n, p))