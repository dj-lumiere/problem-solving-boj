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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        a, b, c = (int(input()) for _ in range(3))
        dots = [[] for _ in range(11)]
        if a == 0:
            # by-c=0 -> y=c/b
            if c % b:
                pass
            else:
                for i in range(1, 11):
                    dots[i].append(c // b)
        elif b == 0:
            # ax-c=0
            if c % a:
                pass
            else:
                dots[c // a].extend(range(1, 11))
        else:
            # y = (c-ax)//b
            for x in range(1, 11):
                y, mod = divmod(c - a * x, b)
                if mod:
                    continue
                elif not 1 <= y <= 10:
                    continue
                dots[x].append(y)
        dots.pop(0)
        for i, v in enumerate(dots):
            if not v:
                dots[i].append(0)
        answer = "\n".join(" ".join(map(str, v)) for v in dots)
        answers.append(f"{answer}")
    print(*answers, sep="\n")