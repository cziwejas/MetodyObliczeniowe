def gauss_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        max_row = i
        for j in range(i+1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        for j in range(i+1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i+1, n+1):
                matrix[j][k] -= factor * matrix[i][k]
            matrix[j][i] = 0
    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for j in range(i):
            matrix[j][n] -= matrix[j][i] * x[i]
    return x


matrix = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

solutions = gauss_elimination(matrix)

print(solutions)
