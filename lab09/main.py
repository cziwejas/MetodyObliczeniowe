import math
import numpy as np
from gauss import gaussian_elimination


def aproksymacja(f, m, n, low, hi, punkt):
    h = (hi - low) / n
    result = 0

    x_vals = [low + i * h for i in range(n + 1)]
    y_vals = [f(i) for i in x_vals]

    matrix = np.zeros((m + 1, m + 1))
    b = np.zeros(m + 1)

    for j in range(m + 1):
        for k in range(m + 1):
            matrix[j][k] = sum(pow(i, k + j) for i in x_vals)

    for k in range(m + 1):
        b[k] = sum(pow(i, k)*j for i, j in zip(x_vals, y_vals))

    gauss_sol = gaussian_elimination(matrix, b)

    for i in range(m + 1):
        result += gauss_sol[i] * pow(punkt, i)

    return result


def f(x):
    return math.sqrt(5*pow(x, 3) - x + 6)


wynik = []
wynik.append(aproksymacja(f, 2, 2, -1, 1, 0.25))
wynik.append(aproksymacja(f, 5, 5, -1, 1, 0.25))
wynik.append(aproksymacja(f, 10, 10, -1, 1, 0.25))
wynik.append(aproksymacja(f, 20, 20, -1, 1, 0.25))
wynik.append(aproksymacja(f, 30, 30, -1, 1, 0.25))
wynik.append(aproksymacja(f, 40, 40, -1, 1, 0.25))
wynik.append(aproksymacja(f, 50, 50, -1, 1, 0.25))

print(wynik)
print(wynik[2])