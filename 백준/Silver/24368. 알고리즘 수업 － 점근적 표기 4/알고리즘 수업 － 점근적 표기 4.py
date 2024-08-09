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
    t = 1
    answers = []
    for hh in range(t):
        a2, a1, a0, c, n0 = (int(input()) for _ in range(5))
        f = lambda x: (a2 - c) * x * x + a1 * x + a0
        fp = lambda x: 2 * (a2 - c) * x + a1
        D = lambda a, b, c: b * b - 4 * a * c
        result = 1
        if a2 - c == 0 and a1 == 0:
            if a0 > 0:
                result = 0
        elif a2 - c == 0 and a1 > 0:
            result = 0
        elif a2 - c == 0 and a1 < 0:
            if -a0 / a1 > n0:
                result = 0
        elif a2 - c < 0:
            if D(a2 - c, a1, a0) > 0 and not (-f(n0) >= 0 and -fp(n0) >= 0):
                result = 0
        elif a2 - c > 0:
            result = 0
        answer = f"{result}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
