import os

tokens = iter(os.read(0, os.fstat(0).st_size).split())
n, m, t = int(next(tokens)), int(next(tokens)), int(next(tokens))
a = [int(next(tokens)) for _ in range(n)]
s = sum(a)
if m != 1:
    k = (t * m ** (m / (m - 1)) / sum(i ** (2 * m / (m - 1)) for i in a)) ** ((m - 1) / m)
    print(s - sum(i ** 2 * (k / m * i ** 2) ** (1 / (m - 1)) for i in a) / s)
elif all([i == a[0] for i in a]):
    print(s - t / n * sum(i ** 2 for i in a) / s)
else:
    x = max(a)
    print(s - x ** 2 * t / s)