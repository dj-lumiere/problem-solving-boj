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
    for hh in range(1, t + 1):
        y0 = int(input())
        m0 = int(input())
        d0 = int(input())
        y1 = int(input())
        m1 = int(input())
        d1 = int(input())
        n = int(input())
        happiness = {}
        for _ in range(n):
            yi, mi, di = int(input()), int(input()), int(input())
            for i in range(200):
                if (y0, m0, d0) <= (yi + i, mi, di) <= (y1, m1, d1):
                    if (yi + i, mi, di) not in happiness:
                        happiness[(yi + i, mi, di)] = 0
                    happiness[(yi + i, mi, di)] += i + 1
        answer = 0
        for k, v in happiness.items():
            if happiness[k] > happiness[(y0, m0, d0)]:
                answer += 1
        answers.append(answer)
    print(*answers, sep="\n")