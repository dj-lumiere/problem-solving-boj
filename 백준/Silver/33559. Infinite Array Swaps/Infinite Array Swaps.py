from sys import stderr, stdout
from collections import Counter

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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        a = [int(input()) for _ in range(n)]
        b = [int(input()) for _ in range(n)]
        count_a = Counter(a)
        count_b = Counter(b)
        overlaps = {}
        for k, v in count_a.items():
            if k in count_b:
                overlaps[k] = min(v, count_b[k])
        a_sort = []
        b_sort = []
        for k, v in overlaps.items():
            a_sort.extend([k] * v)
            b_sort.extend([k] * v)
            count_a[k] -= v
            count_b[k] -= v
        for k, v in count_a.items():
            a_sort.extend([k] * v)
        for k, v in count_b.items():
            b_sort.extend([k] * v)
        answer = f"{sum(overlaps.values())}\n" + " ".join(map(str, a_sort)) + "\n" + " ".join(map(str, b_sort))
        answers.append(answer)
    print(*answers, sep="\n")