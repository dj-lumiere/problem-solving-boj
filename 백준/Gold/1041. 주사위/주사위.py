from itertools import combinations
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
        dice = [int(input()) for _ in range(6)]
        opposing_side = [(0, 5), (1, 4), (2, 3)]
        possible_3c_combination = [x for x in combinations(range(6), r=3) if
                                   not any(i in x and j in x for i, j in opposing_side)]
        possible_2c_combination = [x for x in combinations(range(6), r=2) if
                                   not any(i in x and j in x for i, j in opposing_side)]
        count_5c = 0
        count_3c = 0
        count_2c = 0
        count_1c = 0
        count_0c = 0
        if n == 1:
            count_5c = 1
        elif n == 2:
            count_3c = 4
            count_2c = 4
        else:
            count_3c = 4
            count_2c = (n - 2) * 8 + 4
            count_1c = 5 * (n - 2) ** 2 + (n - 2) * 4
            count_0c = (n - 2) ** 2
        sum_5c_max = sum(dice) - max(dice)
        sum_3c_max = min([dice[i] + dice[j] + dice[k] for i, j, k in possible_3c_combination])
        sum_2c_max = min([dice[i] + dice[j] for i, j in possible_2c_combination])
        sum_1c_max = min(dice)
        answer = sum_5c_max * count_5c + sum_3c_max * count_3c + sum_2c_max * count_2c + sum_1c_max * count_1c
        answers.append(f"{answer}")
    print(*answers, sep="\n")
