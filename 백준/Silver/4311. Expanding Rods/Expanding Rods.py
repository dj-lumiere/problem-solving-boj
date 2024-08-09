from math import pi, sin, cos
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(t):
        l, n, c = (float(input()) for _ in range(3))
        if l < 0 and n < 0 and c < 0:
            break
        l_prime = (1 + n * c) * l
        if l_prime == l:
            result = 0
        else:
            f = lambda x: sin(x) / x - (1 / (1 + n * c))
            fp = lambda x: -sin(x) / x ** 2 + cos(x) / x
            theta = pi / 4
            while True:
                next_theta = theta - f(theta) / fp(theta)
                if abs(theta - next_theta) < 10 ** -7:
                    break
                theta = next_theta
            r = l_prime / 2 / theta
            result = r * (1 - cos(theta))
        answer = f"{result:.3f}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
