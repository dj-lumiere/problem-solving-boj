from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_009
    t = 1
    answers = []
    for hh in range(t):
        X, Y = int(input()), int(input())
        K = int(input())
        route = input()
        pos_x, pos_y = 0, 0
        times = []
        if max(abs(pos_x - X), abs(pos_y - Y)) <= 1:
            times.append(0)
        for time, move in enumerate(route, start=1):
            if move == 'I':
                pos_x += 1
            elif move == 'S':
                pos_y += 1
            elif move == 'Z':
                pos_x -= 1
            elif move == 'J':
                pos_y -= 1
            if max(abs(pos_x - X), abs(pos_y - Y)) <= 1:
                times.append(time)
        if times:
            answer = "\n".join(map(str, sorted(times)))
        else:
            answer = "-1"
        answers.append(f"{answer}")
    print(*answers, sep="\n")