def gaussian_elimination(A, b):

    n = len(b)

    for i in range(n):
        max_idx = i
        max_val = abs(A[i][i])
        for j in range(i + 1, n):
            if abs(A[j][i]) > max_val:
                max_idx = j
                max_val = abs(A[j][i])
        if max_val == 0:
            return None
        if max_idx != i:
            A[i], A[max_idx] = A[max_idx], A[i]
            b[i], b[max_idx] = b[max_idx], b[i]
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i + 1, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    x = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]
    return x


def spline_interpolation(x, y, x_new):

    n = len(x)
    h = [x[i + 1] - x[i] for i in range(n - 1)]
    A = [[0 for j in range(n)] for i in range(n)]
    b = [0 for i in range(n)]
    A[0][0] = 1
    A[n - 1][n - 1] = 1
    for i in range(1, n - 1):
        A[i][i - 1] = h[i - 1]
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        b[i] = 3 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
    c = [0 for i in range(n)]
    c = gaussian_elimination(A, b)
    d = [(c[i + 1] - c[i]) / (3 * h[i]) for i in range(n - 1)]
    b = [(y[i + 1] - y[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3 for i in range(n - 1)]
    a = [y[i] for i in range(n - 1)]

    for i in range(n - 1):
        if x_new >= x[i] and x_new <= x[i + 1]:
            S = a[i] + b[i] * (x_new - x[i]) + c[i] * (x_new - x[i]) ** 2 + d[i] * (x_new - x[i]) ** 3
            break
    return S

x = [-4, -2, 0, 2, 4]
y = [1034, 56, -2, 44, 914]

x_new = 1.0
S = spline_interpolation(x, y, x_new)
print(f"The value of the polynomial at {x_new} is {S}")
