from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
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
        w, h, p, q, r = (int(input()) for _ in range(5))
        x, y = p + r, q + r
        grid_through_x = x // w - p // w
        grid_through_y = y // h - q // h
        x, y = x % w, y % h
        if grid_through_x & 1:
            x = w - x
        if grid_through_y & 1:
            y = h - y
        answer = f"{x} {y}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")
