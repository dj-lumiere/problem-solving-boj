from sys import setrecursionlimit, stdout, stderr

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
    for hh in range(1, t + 1):
        n = int(input())
        p = int(input())
        q = int(input())
        results = dict()
        results[0] = 1
        stack = [n]
        while stack:
            x = stack.pop()
            if x == 0:
                continue
            if x // p in results and x // q in results:
                results[x] = results[x // p] + results[x // q]
                continue
            if x in results:
                continue
            if x not in results:
                results[x] = 0
            stack.append(x)
            for y in {x // p, x // q}:
                stack.append(y)
        answer = results[n]
        answers.append(answer)
    print(*answers, sep="\n")
