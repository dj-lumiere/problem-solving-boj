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
        D = int(input())
        R = int(input())
        T = int(input())
        total = R + T
        answer = 0
        for r in range(4, 201):
            t_age = r - D
            if t_age < 3:
                continue
            S_r = (r * (r + 1)) // 2 - 6
            S_t = (t_age * (t_age + 1)) // 2 - 3
            if S_r + S_t == total:
                answer = R - S_r
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")