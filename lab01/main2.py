def gaussian_elimination(A, b):
    # Augment the matrix A with the vector b
    Ab = []
    for i in range(len(A)):
        Ab.append(A[i] + [b[i]])

    # Perform forward elimination
    n = len(Ab)
    for i in range(n):
        # Find pivot row
        max_row = i
        for j in range(i + 1, n):
            if abs(Ab[j][i]) > abs(Ab[max_row][i]):
                max_row = j
        Ab[i], Ab[max_row] = Ab[max_row], Ab[i]

        # Eliminate column i from rows below pivot
        for j in range(i + 1, n):
            factor = Ab[j][i] / Ab[i][i]
            for k in range(i + 1, n + 1):
                Ab[j][k] -= factor * Ab[i][k]
            Ab[j][i] = 0

    # Perform back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][n] / Ab[i][i]
        for j in range(i):
            Ab[j][n] -= Ab[j][i] * x[i]
            Ab[j][i] = 0

    return x


A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]

x = gaussian_elimination(A, b)

print(x) # output: [2.0, 3.0, -1.0]
