from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30

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
        A = [list(map(int, [input() for _ in range(5)])) for _ in range(5)]
        B = [list(map(int, [input() for _ in range(5)])) for _ in range(5)]
        names = ["Inseo", "Junsuk", "Jungwoo", "Jinwoo", "Youngki"]
        workloads = []
        for x in range(5):
            total = 0
            for y in range(5):
                workload = 0
                for i in range(5):
                    workload += A[x][i] * B[i][y]
                total += workload
            workloads.append(total)
        min_workload = min(workloads)
        candidates = [i for i, w in enumerate(workloads) if w == min_workload]
        priority = [4, 3, 2, 1, 0]
        for p in priority:
            if p in candidates:
                answer = names[p]
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")