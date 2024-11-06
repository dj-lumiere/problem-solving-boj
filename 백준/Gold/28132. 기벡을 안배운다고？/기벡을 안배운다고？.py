from math import gcd
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = 1
    for hh in range(t):
        n = int(input())
        vectors = [(int(input()), int(input())) for _ in range(n)]
        answer = 0
        slope_info = {}
        for x, y in vectors:
            # keep x non negative!
            refined = [x, y]
            if x == y == 0:
                refined = [0, 0]
            elif x == 0:
                refined = [x, 1]
            elif y == 0:
                refined = [1, y]
            else:
                if refined[0] < 0:
                    refined = [-x, -y]
                g = gcd(*refined)
                refined = [refined[0] // g, refined[1] // g]
            if tuple(refined) not in slope_info:
                slope_info[tuple(refined)] = 0
            slope_info[tuple(refined)] += 1
        for (x, y), v in slope_info.items():
            if (x, y) == (0, 0):
                answer += v * (n - 1)
            elif (x, y) == (1, 0):
                answer += v * (slope_info.get((0, 1), 0) + slope_info.get((0, 0), 0))
            elif (x, y) == (0, 1):
                answer += v * (slope_info.get((1, 0), 0) + slope_info.get((0, 0), 0))
            else:
                answer += v * (slope_info.get((y, -x) if y >= 0 else (-y, x), 0) + slope_info.get((0, 0), 0))
        answer //= 2
        answers.append(f"{answer}")
    print(*answers, sep="\n")
