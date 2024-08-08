from itertools import permutations
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        grid = [[int(input()) for _ in range(9)] for _ in range(n)]
        answer = 0
        for order in permutations(range(1, 9)):
            current_index = 0
            score = 0
            for v in grid:
                out_count = 0
                first, second, third = False, False, False
                while out_count < 3:
                    if current_index == 3:
                        current_order = 0
                    elif current_index < 3:
                        current_order = order[current_index]
                    else:
                        current_order = order[current_index - 1]
                    current_result = v[current_order]
                    current_index += 1
                    current_index %= 9
                    if current_result == 0:
                        out_count += 1
                    elif current_result == 1:
                        reached_home = third
                        first, second, third = True, first, second
                        score += reached_home
                    elif current_result == 2:
                        reached_home = second + third
                        first, second, third = False, True, first
                        score += reached_home
                    elif current_result == 3:
                        reached_home = first + second + third
                        first, second, third = False, False, True
                        score += reached_home
                    elif current_result == 4:
                        reached_home = first + second + third
                        first, second, third = False, False, False
                        score += reached_home + 1
            answer = max(score, answer)
        answers.append(f"{answer}")
    print(*answers, sep="\n")
