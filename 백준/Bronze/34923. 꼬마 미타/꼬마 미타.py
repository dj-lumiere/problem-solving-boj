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
        broken_time = input()
        broken_time_actual = (int(broken_time[:2]), int(broken_time[3:]))
        normal_time = input()
        normal_time_actual = (int(normal_time[:2]), int(normal_time[3:]))
        answer1 = broken_time_actual[0] * 60 + broken_time_actual[1] - normal_time_actual[0] * 60 - normal_time_actual[1]
        answer2 = normal_time_actual[0] * 60 + normal_time_actual[1] - broken_time_actual[0] * 60 - broken_time_actual[1]
        if answer1 < 0:
            answer1 += 12 * 60
        if answer2 < 0:
            answer2 += 12 * 60
        answer3 = answer1 if answer1 < answer2 else answer2
        answers.append(answer3 * 6)
    print(*answers, sep="\n")
