def newton_interpolation(x, x_values, y_values):
    n = len(x_values)
    F = [[0] * n for i in range(n)]

    for i in range(n):
        F[i][0] = y_values[i]

    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i+1][j-1] - F[i][j-1]) / (x_values[i+j] - x_values[i])

    result = F[0][0]
    for j in range(1, n):
        product = 1
        for i in range(j):
            product *= (x - x_values[i])
        result += F[0][j] * product

    return result

x_values = [-4, -2, 0, 2, 4]
y_values = [-350, -18, 2, -50, -702]
x = 1

result = newton_interpolation(x, x_values, y_values)
print("Wartość interpolacji dla x = {} wynosi: {}".format(x, result))
