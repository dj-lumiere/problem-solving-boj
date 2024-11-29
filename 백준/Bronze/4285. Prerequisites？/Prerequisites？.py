from decimal import Decimal
from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = INF
    answers = []
    for hh in range(t):
        first = input()
        if first == '0':
            break
        k, m = int(first), int(input())
        selected = set(int(input()) for _ in range(k))
        meets = True
        for _ in range(m):
            parts = []
            while len(parts) < 2:
                parts += [int(x) for x in input().split()]
            c, r = parts[0], parts[1]
            while len(parts) < 2 + c:
                parts += [int(x) for x in input().split()]
            courses = parts[2:2+c]
            count = sum(1 for course in courses if course in selected)
            if count < r:
                meets = False
        answer = "yes" if meets else "no"
        answers.append(f"{answer}")
    print(*answers, sep="\n")