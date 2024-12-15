from fractions import Fraction
from math import isqrt
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
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
        N = int(input())
        duty_hours = {}
        for _ in range(N):
            time_slots = [list(input().split()) for _ in range(4)]
            hours = [4, 6, 4, 10]
            for slot, hour in zip(time_slots, hours):
                for name in slot:
                    if name == "-":
                        continue
                    duty_hours[name] = duty_hours.get(name, 0) + hour
        if not duty_hours:
            answer = "Yes"
        else:
            max_hours = max(duty_hours.values())
            min_hours = min(duty_hours.values())
            if max_hours - min_hours <= 12:
                answer = "Yes"
            else:
                answer = "No"
        answers.append(f"{answer}")
    print(*answers, sep="\n")