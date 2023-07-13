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


def kwadratura(funkcja, low, hi, n):
    if n == 2:
        wagi = [1, 1]
        wezly = [-0.57735, 0.57735]
    elif n == 4:
        wagi = [0.65214, 0.65214, 0.34785, 0.34785]
        wezly = [-0.33998, 0.33998, -0.86113, 0.86113]
    elif n == 6:
        wagi = [0.36076, 0.36076, 0.46791, 0.46791, 0.17132, 0.17132]
        wezly = [0.66120, -0.66120, -0.23861, 0.23861, -0.93246, 0.93246]
    elif n == 8:
        wagi = [0.36268, 0.36268, 0.31370, 0.31370, 0.22238, 0.22238, 0.10122, 0.10122]
        wezly = [-0.18343, 0.18343, -0.52553, 0.52553, -0.79666, 0.79666, -0.96028,
                 0.96028]
    elif n == 10:
        wagi = [0.29552, 0.29552, 0.26926, 0.26926, 0.21908, 0.21908, 0.14945, 0.14945,
                0.06667, 0.06667]
        wezly = [-0.14887, 0.14887, -0.43339, 0.43339, -0.67940, 0.67940, -0.86506,
                 0.86506, -0.97390, 0.97390]
    elif n == 16:
        wagi = [0.18945, 0.18945, 0.18260, 0.18260, 0.16915, 0.16915, 0.14959, 0.14959,
                0.12462, 0.12462, 0.09515, 0.09515, 0.06225, 0.06225, 0.02715, 0.02715]
        wezly = [-0.09501, 0.09501, -0.28160, 0.28160, -0.45801, 0.45801, -0.61787,
                 0.61787,
                 -0.75540, 0.75540, -0.86563, 0.86563, -0.94457, 0.94457, -0.98940,
                 0.98940]
    else:
        raise ValueError("niepoprawne n: do wyboru : [2, 4, 6, 8, 10, 16]")

    suma = 0
    h1 = (hi - low) / 2
    h2 = (hi + low) / 2

    for i in range(0, n):
        suma += wagi[i] * funkcja(h1 * wezly[i] + h2)
    result = h1 * suma

    return result
