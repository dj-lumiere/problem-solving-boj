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
    t = INF
    answers = []
    for _ in range(t):
        line = input()
        if line == "0+0=0":
            answers.append("True")
            break
        parts = line.split('+')
        a = parts[0][::-1]
        b, c = parts[1].split('=')
        b = b[::-1]
        c = c[::-1]
        a_val = int(a)
        b_val = int(b)
        c_val = int(c)
        answer = "True" if a_val + b_val == c_val else "False"
        answers.append(f"{answer}")
    print(*answers, sep="\n")