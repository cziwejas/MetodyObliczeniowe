def iloraz_roznicowy(x, y):
    n = len(x)

    if n == 1:
        return y[0]
    else:
        return (iloraz_roznicowy(x[1:], y[1:]) - iloraz_roznicowy(x[:-1], y[:-1])) / (x[-1] - x[0])

def wartosc_wielomianu_newtona(x, y, xp):

    n = len(x) - 1
    q = [y[0]]
    for i in range(n):
        q.append(iloraz_roznicowy(x[:i+2], y[:i+2]))
    wynik = q[-1]
    for i in range(n-1, -1, -1):
        wynik = q[i] + (xp - x[i]) * wynik

    return wynik

xp = [-4, -2, 0 , 2, 4]
yp = [1034, 56, -2, 44, 914]

print(wartosc_wielomianu_newtona(xp, yp, 1))
