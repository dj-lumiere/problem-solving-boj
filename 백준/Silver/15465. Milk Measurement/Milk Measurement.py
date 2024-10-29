from bisect import bisect_left, bisect_right
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
    MOD = 1_000_000_007
    t = 1
    answers = []
    for hh in range(t):
        N = int(input())
        measurements = []
        for _ in range(N):
            day, cow, change = int(input()), input(), int(input())
            measurements.append((day, cow, change))
        measurements.sort()
        milk = {'Bessie': 7, 'Elsie': 7, 'Mildred': 7}
        display = {'Bessie', 'Elsie', 'Mildred'}
        changes = 0
        for day, cow, change in measurements:
            milk[cow] += change
            max_milk = max(milk.values())
            current_display = set([c for c in milk if milk[c] == max_milk])
            if current_display != display:
                changes += 1
                display = current_display
        answer = changes
        answers.append(f"{answer}")
    print(*answers, sep="\n")