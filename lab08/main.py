import math
import numpy as np
from gauss import kwadratura, gaussian_elimination


def aproksymacja(funkcja, punkt, low, hi, n):
    matrix = np.zeros((n + 1, n + 1))
    b = np.zeros((n + 1))
    result = 0

    for i in range(0, n + 1):
        for j in range(0, n + 1):
            fun = lambda x: pow(x, i) * pow(x, j)
            matrix[i][j] = kwadratura(fun, low, hi, 16)

    for i in range(0, n + 1):
        fun = lambda x: pow(x, i) * funkcja(x)
        b[i] = kwadratura(fun, low, hi, 16)

    gauss = gaussian_elimination(matrix, b)

    for i in range(0, n + 1):
        result += pow(punkt, i) * gauss[i]

    return result


def f(x):
    return math.sqrt(5*pow(x, 3) - x + 6)

wynik = []
wynik.append(aproksymacja(f, 0.25, -1, 1, 10))
wynik.append(aproksymacja(f, 0.25, -1, 1, 20))
wynik.append(aproksymacja(f, 0.25, -1, 1, 30))
wynik.append(aproksymacja(f, 0.25, -1, 1, 40))
wynik.append(aproksymacja(f, 0.25, -1, 1, 50))
print(wynik)