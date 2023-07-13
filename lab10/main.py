from gauss import kwadratura
import numpy as np
import math


def leg(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * leg(n - 1, x) - (n - 1) * leg(n - 2, x)) / n


def aproksymacja(funkcja, low, hi, n, punkt):

    lmbd = np.zeros(n + 1)
    c = np.zeros(n + 1)
    result = 0

    for i in range(n + 1):
        fun = lambda x: pow(leg(i, x), 2)
        lmbd[i] = kwadratura(fun, low, hi, 16)

    for i in range(n + 1):
        fun = lambda x: funkcja(x) * leg(i, x)
        c[i] = kwadratura(fun, low, hi, 16)/lmbd[i]

    for i in range(n + 1):
        result += c[i]*leg(i, punkt)

    return result


def f(x):
    return math.sqrt(5*pow(x, 3) - x + 6)


wynik = []
wynik.append(aproksymacja(f, -1, 1, 1, 0.25))
wynik.append(aproksymacja(f, -1, 1, 2, 0.25))
wynik.append(aproksymacja(f, -1, 1, 3, 0.25))
wynik.append(aproksymacja(f, -1, 1, 4, 0.25))
wynik.append(aproksymacja(f, -1, 1, 5, 0.25))
print(wynik)
print(wynik[-1])