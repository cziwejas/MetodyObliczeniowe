def f(x):
    return -24*pow(x, 2)-10*x+25


def bisekcja(f, low, hi, epsilon):
    if f(low) * f(hi) >= 0:
        raise ValueError("warunki zbieżności nie są spełnione")

    iter_count = 0
    while abs(hi - low) > epsilon:
        x = (low + hi) / 2
        if f(x) == 0:
            return x
        elif f(x) * f(low) < 0:
            hi = x
        else:
            low = x

        iter_count += 1

    res = (low+hi)/2
    wyniki = [res, iter_count]

    return wyniki

print(bisekcja(f, 0.5, 5, 1e-5))


wyniki = []

wyniki.append(bisekcja(f, 0.5, 5, 1e-2))
wyniki.append(bisekcja(f, 0.5, 5, 1e-3))
wyniki.append(bisekcja(f, 0.5, 5, 1e-5))
wyniki.append(bisekcja(f, 0.5, 5, 1e-10))
wyniki.append(bisekcja(f, 0.5, 5, 1e-15))

print(wyniki)

