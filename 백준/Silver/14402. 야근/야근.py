from collections import defaultdict
from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for _ in range(t):
        q = int(input())
        counts = defaultdict(lambda: 0)
        stack = defaultdict(lambda: [])
        for _ in range(q):
            s, p = input(), input()
            if stack[s] and stack[s][-1] == "+" and p == "-":
                stack[s].pop()
            elif p == "-":
                counts[s] += 1
            elif p == "+":
                stack[s].append(p)
        for k, v in stack.items():
            counts[k] += len(v)
        total = 0
        for v in counts.values():
            total += v
        answer = total
        answers.append(f"{answer}")
    print(*answers, sep="\n")