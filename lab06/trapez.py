import math


def metoda_trapezow(funkcja, a, b, n):

    h = (b - a) / n

    xp = [a + i * h for i in range(n+1)]
    yp = [funkcja(xi) for xi in xp]

    suma = sum(yp[1:-1])

    return h * (yp[0]/2 + suma + yp[-1]/2)


def f(x):
    return (math.sin(0.7*x + 0.1))/(1.3 + math.cos(pow(x,2) + 0.2))


calka1 = metoda_trapezow(f, 0.3, 1.1, 2)
calka2 = metoda_trapezow(f, 0.3, 1.1, 10)
calka3 = metoda_trapezow(f, 0.3, 1.1, 100)
calka4 = metoda_trapezow(f, 0.3, 1.1, 1000)
calka5 = metoda_trapezow(f, 0.3, 1.1, 10000)

calki = [calka1, calka2, calka3, calka4, calka5]

print(calki)