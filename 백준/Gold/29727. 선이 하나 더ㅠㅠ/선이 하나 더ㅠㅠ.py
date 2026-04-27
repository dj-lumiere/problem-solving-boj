from math import comb
import os

tokens = iter(os.read(0, os.fstat(0).st_size).split())
# tokens = iter("3 -1 -1 -1 3".split())
n, xa, ya, xb, yb = map(int, tokens)
INF = 10 ** 18
(xa, ya), (xb, yb) = sorted(((xa, ya), (xb, yb)))
slope = (yb - ya) / (xb - xa) if xa != xb else INF
result = comb(n + 1, 2) ** 2
if slope != 0 and slope != INF:
    pass
elif slope == 0:
    if xa < 0 and xb >= n:
        result += comb(n + 1, 2) * (n + 1)
    elif xa < 0 and 0 <= xb < n:
        result += comb(xb + 1, 2) * (n + 1)
    elif xb >= n and 0 <= xa < n:
        result += comb(n - xa, 2) * (n + 1)
    elif 0 <= xa <= xb < n:
        result += comb(xb - xa, 2) * (n + 1)
elif slope == INF:
    if ya < 0 and yb >= n:
        result += comb(n + 1, 2) * (n + 1)
    elif ya < 0 and 0 <= yb < n:
        result += comb(yb + 1, 2) * (n + 1)
    elif yb >= n and 0 <= ya < n:
        result += comb(n - ya, 2) * (n + 1)
    elif 0 <= ya <= yb < n:
        result += comb(abs(yb - ya), 2) * (n + 1)
print(result)