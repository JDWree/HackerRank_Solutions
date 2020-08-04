# Task:
# Andrea has a simple equation:
#           Y = a + b1.f1 + b2.f2 + ... + bm.fm
# for (m+1) real constants (a, f1, f2, ..., fm).
# We can say that the value of 'Y' depends on 'm' features.
# Andrea studies this equation for 'n' different feature sets (f1,f2,...,fm)
# and records each respective value of 'Y'. If she has 'q' new feature sets,
# can you help Andrea find the value of 'Y' for each of the sets?
# Note: You are not expected to account for bias and variance trade-offs.

m,n = (map(int, input().rstrip().split()))
X, Y = [], []

for _ in range(n):
    row = list(map(float, input().rstrip().split()))
    X.append([1] + row[:-1])
    Y.append([row[-1]])

q = int(input().rstrip())
X_q = []

for _ in range(q):
    X_q.append([1] + list(map(float,input().rstrip().split())))


def transpose(m):
    """Returns the transposed matrix."""
    rows = len(m)
    cols = len(m[0])

    m_T = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            m_T[j][i] = m[i][j]

    return m_T

def copy_matrix(m):
    """Creates a copy of a matrix."""
    rows = len(m)
    cols = len(m[0])

    m_copy = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            m_copy[i][j] = m[i][j]

    return m_copy

def matrix_dotproduct(m,A):
    """Returns the resulting matrix of the dot product between the two given matrices.
    Returns 'None' when dimensions are not compatible."""
    rows_m = len(m)
    cols_m = len(m[0])

    rows_A = len(A)
    cols_A = len(A[0])

    if cols_m != rows_A:
        print("Error!: Dimensions of the matrices aren't compatible for a dot product!")
        print(f"m ({rows_m} x {cols_m}) . A ({rows_A} x {cols_A})")
        print("Returned 'None'.")
        return None

    m_dot_A = [[0 for _ in range(cols_A)] for _ in range(rows_m)]

    for i in range(rows_m):
        for j in range(cols_A):
            row_dot_col = 0
            for k in range(cols_m):
                row_dot_col += m[i][k] * A[k][j]
            m_dot_A[i][j] = row_dot_col

    return m_dot_A



def inverse_matrix(m):
    """Creates the inverse matrix."""
    rows = len(m)
    cols = len(m[0])

    if rows != cols:
        print("Error! Matrix has to be square!")
        return m
    m_copy = copy_matrix(m)
    # Creating identity matrix
    Im = [[1 if i == k else 0 for k in range(cols)] for i in range(rows)]

    # Spil method:
    #   - make diagonal element 1 by dividing row by value of diagonal element
    #   - make elements x in column of diagonal element 0
    #       by subtracting x*(diagonal value) from each row
    #   - repeat for all diagonal elements
    #   - Do every step with the identity matrix too.
    #   - A.A(-1) = I --> (A --> I, will make I --> A(-1))

    for i in range(rows):
        Im[i] = [Im[i][j]/m_copy[i][i] for j in range(cols)]
        m_copy[i] = [m_copy[i][j]/m_copy[i][i] for j in range(cols)]
        for j in range(rows):
            if j != i:
                Im[j] = [Im[j][k] - m_copy[j][i]*Im[i][k] for k in range(cols)]
                m_copy[j] = [m_copy[j][k] - m_copy[j][i]*m_copy[i][k] for k in range(cols)]

    return Im

# B = (X_T . X)^(-1) . X_T . Y
X_T = transpose(X)
X_inv = inverse_matrix(matrix_dotproduct(X_T, X))
X_product = matrix_dotproduct(X_inv, X_T)
B = matrix_dotproduct(X_product, Y)

for row in X_q:
    print(f"{matrix_dotproduct([row], B)[0][0]:.2f}")


# NOT USED

# def shift_rows(m):
#     """Shifts the rows of the matrix such that all diagonal elements
#      are not zero (if possible)."""
#     m_copy = copy_matrix(m)
#     rows = len(m)
#     cols = len(m[0])

#     if rows != cols:
#         print("Error! Matrix has to be square.")
#         print("Given matrix returned.")
#         return m

#     zero = False
#     for i in range(rows):

#         if m_copy[i][i] == 0:
#             zero = True
#             found = False
#             if i != 0:
#                 for j in range(i-1,-1,-1):
#                     if m_copy[j][i] != 0 and m_copy[i][j] != 0:
#                         row = m_copy[i]
#                         m_copy[i] = m_copy[j]
#                         m_copy[j] = row
#                         found = True
#                         break
#                 if not found and i != rows:
#                     for j in range(i+1,rows-i):
#                         if m_copy[j][i] != 0 and m_copy[i][j] != 0:
#                             m_copy[i] = m_copy[j]
#                             m_copy[j] = m_copy[i]
#                             found = True
#                             break
#             else:
#                 for j in range(1,rows):
#                         if m_copy[j][i] != 0 and m_copy[i][j] != 0:
#                             m_copy[i] = m_copy[j]
#                             m_copy[j] = m_copy[i]
#                             found = True
#                             break

#     if zero and not found:
#         print("Unable to make all diagonal elements none zero.")
#     # elif not zero:
#     #     print("All diagonal elements were already none zero.")

#     return m_copy

# def row_operation(row, operation, value):
#     """Do element wise operation over a list."""
#     if operation == "add":
#         return [row[i] + value for i in range(len(row))]
#     elif operation == "sub":
#         return [row[i] - value for i in range(len(row))]
#     elif operation == "div":
#         return [row[i] / value for i in range(len(row))]
#     elif operation == "mul":
#         return [row[i] * value for i in range(len(row))]
