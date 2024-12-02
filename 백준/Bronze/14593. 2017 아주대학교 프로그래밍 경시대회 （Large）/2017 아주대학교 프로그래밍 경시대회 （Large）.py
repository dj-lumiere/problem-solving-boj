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
        N = int(input())
        best_Si = -1
        best_Ci = 51
        best_Li = 180
        best_idx = 1
        for i in range(1, N + 1):
            Si = int(input())
            Ci = int(input())
            Li = int(input())
            if Si > best_Si or (Si == best_Si and (Ci < best_Ci or (Ci == best_Ci and Li < best_Li))):
                best_Si = Si
                best_Ci = Ci
                best_Li = Li
                best_idx = i
        answer = str(best_idx)
        answers.append(f"{answer}")
    print(*answers, sep="\n")