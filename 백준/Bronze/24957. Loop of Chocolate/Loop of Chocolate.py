from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    pi = Decimal('3.141592653589793238462643383279')
    for hh in range(t):
        n = int(input())
        r = int(input())
        centers = []
        for _ in range(n):
            x = int(input())
            y = int(input())
            z = int(input())
            centers.append((x, y, z))
        sphere_volume = Decimal('4') / Decimal('3') * pi * Decimal(r) ** 3
        intersection_volume = Decimal('0')
        for i in range(n):
            x1, y1, z1 = centers[i]
            x2, y2, z2 = centers[(i + 1) % n]
            dx = Decimal(x1 - x2)
            dy = Decimal(y1 - y2)
            dz = Decimal(z1 - z2)
            d = (dx ** 2 + dy ** 2 + dz ** 2).sqrt()
            vol = (Decimal('2') / Decimal('3')) * pi * (Decimal(r) - d / Decimal('2')) ** 2 * (Decimal('2') * Decimal(r) + d / Decimal('2'))
            intersection_volume += vol
        union_volume = Decimal(n) * sphere_volume - intersection_volume
        answer = f"{union_volume}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
