from bisect import bisect_left
from math import pi
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
    MOD = 998_244_353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        w = [int(input()) for _ in range(n)]
        w.sort()
        answer = 0
        current_weight_sum = 0
        current_index = 0
        current_weights = []
        while current_index < n:
            current_weight_sum += w[current_index]
            current_weights.append(w[current_index])
            answer += 1
            next_index = bisect_left(w, current_weight_sum)
            if current_index == next_index:
                next_index += 1
            current_index = next_index
        eprint(current_weights)
        answers.append(answer)
    print(*answers, sep="\n")
