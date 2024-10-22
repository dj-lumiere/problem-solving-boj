from sys import setrecursionlimit, stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(1, t + 1):
        number_count = [0, 0, 0, 0]
        s, l, r, n = (int(input()) for _ in range(4))
        r += 1
        next_stage = [[], [1, 3, 2], [2, 1, 1], [2, 3, 2]]
        stage = [[[0, 0, 0, 0] for _ in range(4)] for _ in range(n + 1)]
        for h in range(1, 4):
            stage[0][h][h] += 1
            for i in range(1, n + 1):
                stage[i][h][1] = stage[i - 1][h][1] + 2 * stage[i - 1][h][2]
                stage[i][h][2] = stage[i - 1][h][1] + stage[i - 1][h][2] + 2 * stage[i - 1][h][3]
                stage[i][h][3] = stage[i - 1][h][1] + stage[i - 1][h][3]
        stack = [(l, r, 0, 3 ** n, n, s)]
        while stack:
            # real left, real right, lower bound, upper bound, n, start
            cl, cr, ct, cb, cn, cs = stack.pop()
            if cn < 0:
                continue
            if cl == ct and cr == cb:
                for i in range(4):
                    number_count[i] += stage[cn][cs][i]
                continue
            if cn == 0:
                continue
            for i in range(3):
                nt, nb = ct + 3 ** (cn - 1) * i, ct + 3 ** (cn - 1) * (i + 1)
                nl, nr = max(cl, nt), min(cr, nb)
                if nl >= nr:
                    continue
                stack.append((nl, nr, nt, nb, cn - 1, next_stage[cs][i]))
        answer = " ".join(map(str, number_count[1:]))
        answers.append(f"{answer}")
    print(*answers, sep="\n")
