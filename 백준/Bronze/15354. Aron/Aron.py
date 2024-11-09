from decimal import getcontext
from sys import stderr, stdout

getcontext().prec = 30

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
        N = int(input())
        colors = [input() for _ in range(N)]
        groups = []
        current_color = colors[0]
        count = 1
        for color in colors[1:]:
            if color == current_color:
                count += 1
            else:
                groups.append(count)
                current_color = color
                count = 1
        groups.append(count)
        total_people = len(groups)
        answer = total_people + 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")