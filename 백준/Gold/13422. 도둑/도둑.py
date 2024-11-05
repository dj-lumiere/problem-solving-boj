from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(t):
        n, m, k = (int(input()) for _ in range(3))
        a = [int(input()) for _ in range(n)]
        prefix_sum = [0]
        for v in a:
            prefix_sum.append(prefix_sum[-1] + v)
        for v in a[:m]:
            prefix_sum.append(prefix_sum[-1] + v)
        count = 0
        for i in (range(n) if n != m else range(1)):
            score = prefix_sum[i + m] - prefix_sum[i]
            if score < k:
                count += 1
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")