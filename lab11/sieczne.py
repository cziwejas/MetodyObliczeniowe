def f(x):
    return -24*pow(x,2)-10*x+25


def sieczne(f, low, hi, eps, max_iter=1000):
    if f(low) * f(hi) >= 0:
        raise ValueError("warunki zbieżności nie są spełnione")

    iter_count = 0
    while abs(f(hi)) > eps and iter_count < max_iter:
        x_next = hi - f(hi) * (hi - low) / (f(hi) - f(low))

        low = hi
        hi = x_next

        iter_count += 1

    res = hi

    wyniki = [res, iter_count]

    return wyniki

wyniki = []

wyniki.append(sieczne(f, 0.5, 5, 1e-2))
wyniki.append(sieczne(f, 0.5, 5, 1e-3))
wyniki.append(sieczne(f, 0.5, 5, 1e-5))
wyniki.append(sieczne(f, 0.5, 5, 1e-10))
wyniki.append(sieczne(f, 0.5, 5, 1e-15))

print(wyniki)
