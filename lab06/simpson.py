import math


def f(x):
    return (math.sin(0.7*x + 0.1))/(1.3 + math.cos(pow(x, 2) + 0.2))


def metoda_simpsona(funkcja, a, b, n):

    h = (b - a) / n
    x = [a + i * h for i in range(n + 1)]

    suma = 0

    sumakrancowych = funkcja(a) + funkcja(b)

    for i in range(1, n, 2):
        suma += 4 * funkcja(x[i])

    for i in range(2, n-1, 2):
        suma += 2 * funkcja(x[i])

    wynik = (suma + sumakrancowych) * h / 3

    return wynik


calka1 = metoda_simpsona(f, 0.3, 1.1, 2)
calka2 = metoda_simpsona(f, 0.3, 1.1, 10)
calka3 = metoda_simpsona(f, 0.3, 1.1, 100)
calka4 = metoda_simpsona(f, 0.3, 1.1, 1000)
calka5 = metoda_simpsona(f, 0.3, 1.1, 10000)

calki = [calka1, calka2, calka3, calka4, calka5]

print(calki)
