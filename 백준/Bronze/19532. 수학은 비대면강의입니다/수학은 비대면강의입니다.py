# 19532 수학은 비대면강의입니다

from itertools import product

a, b, c, d, e, f = map(int, input().split(" "))

for x, y in product(range(-999, 1000), range(-999, 1000)):
    if a * x + b * y == c and d * x + e * y == f:
        print(x, y)
        break