from itertools import product
from math import floor, log
from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
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
        s = input().replace("()", "!")
        current_bracket = []
        current_laser = []
        pieces = 0
        for i, v in enumerate(s):
            if not current_bracket and v == "!":
                pass
            elif current_bracket and v == "!":
                current_laser[-1] += 1
            elif v == "(":
                current_bracket.append(v)
                current_laser.append(0)
            elif v == ")" and current_bracket:
                current_laser_heap = current_laser.pop()
                current_bracket.pop()
                pieces += current_laser_heap + 1
                if current_laser:
                    current_laser[-1] += current_laser_heap
        answer = pieces
        answers.append(f"{answer}")
    print(*answers, sep="\n")
