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
    DELTA = [(0, 0), (0, -1), (0, 1), (-1, 0), (1, 0)]
    INF = 10 ** 18
    MOD = 998_244_353
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n = int(input())
        k = int(input())
        a = [input() for _ in range(n)]
        current_set = [False for _ in range(1 << k)]
        z = 0
        for idx, i in enumerate(a):
            algorithm_int = int(i[::-1] if z == 1 else i, base=2)
            for j in range(1 << k):
                if algorithm_int & j != algorithm_int:
                    continue
                if current_set[j]:
                    z = 0
                    answers.append("WellKnown")
                    break
            else:
                current_set[algorithm_int] = True
                answers.append("AdHoc")
                z = 1
    print(*answers, sep="\n")