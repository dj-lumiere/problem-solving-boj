from decimal import Decimal
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
        n = int(input())
        runners = [(input(), Decimal(input()), Decimal(input())) for _ in range(n)]
        best_time = INF
        best_team = []
        for i in range(n):
            first_runner = runners[i]
            other_runners = runners[:i] + runners[i + 1:]
            sorted_others = sorted(other_runners, key=lambda x: x[2])
            if len(sorted_others) < 3:
                continue
            total_time = first_runner[1] + sorted_others[0][2] + sorted_others[1][2] + sorted_others[2][2]
            if total_time < best_time:
                best_time = total_time
                best_team = [first_runner[0], sorted_others[0][0], sorted_others[1][0], sorted_others[2][0]]
        answer = f"{best_time:.2f}\n" + "\n".join(best_team)
        answers.append(f"{answer}")
    print(*answers, sep="\n")