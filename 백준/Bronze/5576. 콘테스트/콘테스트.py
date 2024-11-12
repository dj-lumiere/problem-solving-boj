from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        W_scores = [int(input()) for _ in range(10)]
        K_scores = [int(input()) for _ in range(10)]
        W_sum = sum(sorted(W_scores, reverse=True)[:3])
        K_sum = sum(sorted(K_scores, reverse=True)[:3])
        answer = f"{W_sum} {K_sum}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")