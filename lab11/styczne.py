def f(x):
    return -24*pow(x,2)-10*x+25


def poch(x):
    return -48*x-10


def styczne(f, poch, low, hi, epsilon, max_iter=100):
    if f(low) * f(hi) >= 0:
        raise ValueError("warunki zbieżności nie są spełnione")

    x = low
    iter_count = 0

    while abs(f(x)) > epsilon and iter_count < max_iter:
        x = x - f(x) / poch(x)
        iter_count += 1

    wyniki = [x, iter_count]

    return wyniki

wyniki = []

wyniki.append(styczne(f, poch, 0.5, 5, 1e-2))
wyniki.append(styczne(f, poch, 0.5, 5, 1e-3))
wyniki.append(styczne(f, poch, 0.5, 5, 1e-5))
wyniki.append(styczne(f, poch, 0.5, 5, 1e-10))
wyniki.append(styczne(f, poch, 0.5, 5, 1e-15))

print(wyniki)