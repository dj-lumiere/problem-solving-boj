from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        # sum(k*(n//k))-sum(k)-sum(1)
        # harmonic lemma : n//k has at most 2sqrt(n) different values.
        periods = [0]
        for i in range(1, int(n ** .5) + 1):
            j = n // i
            periods.append(i)
            if i == j:
                continue
            periods.append(j)
        periods.sort()
        n_over_k = (periods[1:])[::-1]
        answer = (sum((i + 1 + j) * (j - i) // 2 * k for i, j, k in zip(periods, periods[1:], n_over_k)) - n - n * (
                n + 1) // 2 + 1) % 1000000
        answers.append(f"{answer}")
print(*answers, sep="\n")
