from sys import stderr, stdout

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
        s = int(input())
        possible = []
        for x in range(2, s):
            for y in [x, x - 1]:
                if y < 1:
                    continue
                if (x == 1 and y == s) or (x == s and y == 1):
                    continue
                if s % (x + y) == 0:
                    possible.append((x, y))
                elif (s - x) % (x + y) == 0 and (s - x) // (x + y) >= 1:
                    possible.append((x, y))
        possible = sorted(possible)
        res = [f"{x},{y}" for (x, y) in possible]
        answer = f"{s}:"
        if res:
            answer += "\n" + "\n".join(res)
        answers.append(answer)
    print(*answers, sep="\n")