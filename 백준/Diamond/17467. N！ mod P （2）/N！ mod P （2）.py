from sys import stdout, stderr

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
        n, m = (int(input()), int(input()))
        a1 = 1
        a2 = 1
        for i in range(1, n + 1, 2):
            a1 = a1 * i % m
            if i + 1 > n:
                break
            a2 = a2 * (i + 1) % m
        answer = a1 * a2 % m
        answers.append(f"{answer}")
    print(*answers)
