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
    t = INF
    answers = []
    for hh in range(t):
        X, Y = (int(input()) for _ in range(2))
        if X == 0 and Y == 0:
            break
        M = int(input())
        items = {}
        for _ in range(M):
            xi, yi = int(input()), int(input())
            items[(xi, yi)] = items.get((xi, yi), 0) + 1
        N = int(input())
        total = 0
        for _ in range(N):
            qi, qj = int(input()), int(input())
            total += items.get((qi, qj), 0)
        answer = total
        answers.append(f"{answer}")
    print(*answers, sep="\n")