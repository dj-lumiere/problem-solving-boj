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
    t = INF
    answers = []
    for hh in range(t):
        g = input()
        if g == '#':
            break
        y, m, d = (int(input()) for _ in range(3))
        if y < 31 or (y == 31 and m <=4):
            era = "HEISEI"
            y_new = y
        else:
            era = "?"
            y_new = y - 30
        answer = f"{era} {y_new} {m} {d}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")