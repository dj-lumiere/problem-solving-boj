from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(t):
        width, height = int(input()), int(input())
        cuts = int(input())
        horizontal, vertical = [0, height], [0, width]
        for _ in range(cuts):
            direction, pos = int(input()), int(input())
            if direction == 0:
                horizontal.append(pos)
            else:
                vertical.append(pos)
        horizontal.sort()
        vertical.sort()
        max_h = max(horizontal[i + 1] - horizontal[i] for i in range(len(horizontal) - 1))
        max_v = max(vertical[i + 1] - vertical[i] for i in range(len(vertical) - 1))
        answers.append(max_h * max_v)
    print(*answers, sep="\n")