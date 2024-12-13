from sys import stdout, stderr

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
    for hh in range(t):
        A, B, C = (int(input()) for _ in range(3))
        periods = [tuple(int(input()) for _ in range(2)) for _ in range(3)]
        total = 0
        for minute in range(1, 101):
            cnt = sum(1 for s, e in periods if s <= minute < e)
            if cnt == 1:
                total += A
            elif cnt == 2:
                total += 2 * B
            elif cnt == 3:
                total += 3 * C
        answer = total
        answers.append(f"{answer}")
    print(*answers, sep="\n")