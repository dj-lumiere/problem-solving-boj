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
    t = int(input())
    answers = []
    for _ in range(t):
        n, q = int(input()), int(input())
        L = [int(input()) for _ in range(n)]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + L[i]
        case_answers = []
        for __ in range(q):
            i, j = int(input()), int(input())
            if i > j:
                i, j = j, i
            rsq = prefix[j + 1] - prefix[i]
            case_answers.append(str(rsq))
        answer = '\n'.join(case_answers)
        answers.append(answer)
    print(*answers, sep="\n\n")