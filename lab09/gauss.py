import numpy as np

def gaussian_elimination(A, b):
    n = len(A)

    Ab = np.concatenate((A, b.reshape(n, 1)), axis=1)

    for i in range(n):
        max_el = abs(Ab[i][i])
        max_row = i
        for j in range(i + 1, n):
            if abs(Ab[j][i]) > max_el:
                max_el = abs(Ab[j][i])
                max_row = j

        Ab[[i, max_row]] = Ab[[max_row, i]]

        for j in range(i + 1, n):
            c = -Ab[j][i] / Ab[i][i]
            Ab[j] = Ab[j] + c * Ab[i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = Ab[i][-1] / Ab[i][i]
        for j in range(i - 1, -1, -1):
            Ab[j][-1] -= Ab[j][i] * x[i]

    return x