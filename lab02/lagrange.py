import numpy as np


def interpolation(xp, *args):
    n = len(args)

    x = np.zeros(n)
    y = np.zeros(n)

    for i in range(n):
        x[i] = args[i][0]
        y[i] = args[i][1]

    yp = 0

    for i in range(n):

        p = 1

        for j in range(n):
            if i != j:
                p = p * (xp - x[j]) / (x[i] - x[j])

        yp = yp + p * y[i]

    return yp

print(interpolation(1, [-4, 1034], [-2, 56], [0, -2], [2, 44], [4, 914]))
