from sys import stderr, stdout

with open(0, "r") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    x = int(input())
    answers = []
    for hh in range(1, x + 1):
        n, m = (int(input()) for _ in range(2))
        machines = [[int(input()) for _ in range(4)] for _ in range(m)]
        usage_count = [0] * m
        for _ in range(n):
            usage_count[int(input()) - 1] += 1
        profitable = []
        for i in range(m):
            p, c, u, r = machines[i]
            if min(usage_count[i], u) * r > p + min(usage_count[i], u) * c:
                profitable.append(i + 1)
        profitable.sort()
        answers.append(f"Data Set {hh}:")
        answers.extend(map(str, profitable))
        answers.append("")
    print(*answers, sep="\n")