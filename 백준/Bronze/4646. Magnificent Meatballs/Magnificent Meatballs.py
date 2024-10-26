from collections import deque
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
    MOD = 1_000_000_009
    t = INF
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        if n == 0:
            break
        meatballs = [int(input()) for _ in range(n)]
        total = sum(meatballs)
        if total % 2 != 0:
            answer = "No equal partitioning."
        else:
            target = total // 2
            left_sum, right_sum = 0, 0
            i, j = 0, n - 1
            while i <= j:
                if left_sum < target:
                    left_sum += meatballs[i]
                    i += 1
                elif right_sum < target:
                    right_sum += meatballs[j]
                    j -= 1
                else:
                    break
            answer = f"Sam stops at position {i} and Ella stops at position {j + 2}." if left_sum == right_sum == target else "No equal partitioning."
        answers.append(answer)
    print(*answers, sep="\n")