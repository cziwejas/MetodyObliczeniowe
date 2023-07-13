def silnia(n):
    if n > 1:
        return n*silnia(n-1)
    return 1


def roznicaProgresywna(xi, fi):

    n = len(xi)
    roznice = [fi]
    for i in range(1, n):
        roznice.append([])
        for j in range(n-i):
            roznice[i].append((roznice[i-1][j+1] - roznice[i-1][j]))
    return roznice


def interpolacja_newtona(x, xi, fi):

    h = xi[1] - xi[0]
    n = len(xi)
    roznice = roznicaProgresywna(xi, fi)
    wynik = fi[0]
    iloczyn = 1
    for i in range(1, n):
        iloczyn *= (x - xi[i-1])
        wynik += roznice[i][0]/silnia(i)*pow(h, i) * iloczyn

    return wynik


tabx = [1, 2, 3, 4]
taby = [3, 7, 8, 15]


print(interpolacja_newtona(2.5, tabx, taby))