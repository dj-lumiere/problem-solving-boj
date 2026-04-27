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
    MOD = 998_244_353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n, k = int(input()), int(input())
        a = [0] + [int(input()) for _ in range(n)]
        queries = [(int(input()), int(input())) for _ in range(k)]
        answer = 0
        for i in range(1 << k):
            j = 0
            a2 = a[:]
            while i > 0:
                if i & 1:
                    for k in range(queries[j][0], queries[j][1] + 1):
                        a2[k] ^= 1
                i >>= 1
                j += 1
            answer += sum(a2)
        answer %= MOD
        answers.append(answer)
    print(*answers, sep="\n")