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
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        n, m = int(input()), int(input())
        x = int(''.join(input() for _ in range(m)))
        y = int(''.join(input() for _ in range(m)))
        wheel = [int(input()) for _ in range(n)]
        count = 0
        for i in range(n):
            z = int(''.join(str(wheel[(i + j) % n]) for j in range(m)))
            if x <= z <= y:
                count += 1
        answer = count
        answers.append(answer)
    print(*answers, sep="\n")