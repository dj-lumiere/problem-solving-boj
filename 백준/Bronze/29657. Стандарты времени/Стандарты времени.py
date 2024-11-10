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
    t = 1
    answers = []
    for hh in range(t):
        a1, b1, c1 = int(input()), int(input()), int(input())
        a2, b2, c2 = int(input()), int(input()), int(input())
        h1, m1, s1 = int(input()), int(input()), int(input())
        total_seconds = h1 * b1 * c1 + m1 * c1 + s1
        h2 = total_seconds // (b2 * c2)
        remainder = total_seconds % (b2 * c2)
        m2 = remainder // c2
        s2 = remainder % c2
        answer = f"{h2} {m2} {s2}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")