import numpy as np


def zero_diagonal(matrix):
    new_matrix = np.zeros((len(matrix), len(matrix)))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                new_matrix[i][j] = matrix[i][j]

    return new_matrix


def condition(matrix, sol, eps):
    for i, j in zip(matrix, sol):
        if abs(i - j) > eps:
            return False
    return True


def proste(matrix, sol, eps = 0.001, max_iter = 1000):
    diag = [matrix[i][i] for i in range(len(matrix))]
    appr = np.zeros(len(sol))
    matrix_zero = zero_diagonal(matrix)
    iter_num = 0

    for i in range(max_iter):
        new_appr = (sol - np.dot(matrix_zero, appr)) / diag
        if condition(appr, new_appr, eps):
            break
        appr = new_appr
        iter_num += 1

    return list(appr), iter_num


matrix = [
    [5, -5, -1, 1],
    [-15, 16, 0, -5],
    [25, -29, 11, 17],
    [15, -12, -8, -4]
]

sol = [-5, 27, -97, 12]

A = np.array([
    [3, 1, 2],
    [1, -4, 1],
    [1, 2, 3]
])
b = np.array([5, -7, 2])

print(proste(matrix, sol))
