from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = int(input())
    answers = []
    for hh in range(t):
        result = input().split(':')
        a = int(result[0])
        b = int(result[1])
        total_lag_wins = 0
        total_dcu_wins = 0
        for c in range(0, 10):
            for d in range(0, 10):
                sum_lag = a + d
                sum_dcu = b + c
                if sum_lag > sum_dcu:
                    total_lag_wins += 1
                elif sum_dcu > sum_lag:
                    total_dcu_wins += 1
                else:
                    if d > b:
                        total_lag_wins += 1
                    elif b > d:
                        total_dcu_wins += 1
        answer = f"{total_lag_wins} {total_dcu_wins}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")