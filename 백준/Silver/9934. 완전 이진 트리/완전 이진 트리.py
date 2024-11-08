from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    answers = []
    t = 1
    for hh in range(t):
        K = int(input())
        A = [int(input()) for _ in range(2 ** K - 1)]
        levels = [[] for i in range(K)]
        stack = [(K - 1, 2 ** (K - 1) - 1)]
        while stack:
            level, offset = stack.pop()
            levels[level].append(A[offset])
            if level == 0:
                continue
            stack.append((level - 1, offset + 2 ** (level - 1)))
            stack.append((level - 1, offset - 2 ** (level - 1)))
        levels.reverse()
        answer = "\n".join(" ".join(map(str, v)) for v in levels)
        answers.append(f"{answer}")
    print(*answers)
