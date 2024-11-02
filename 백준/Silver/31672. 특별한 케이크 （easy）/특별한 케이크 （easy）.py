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
        first_line = [input(), input(), input(), input()]
        n = int(input())
        statements = []
        for _ in range(n):
            m = int(input())
            s = set(int(input()) for _ in range(m))
            b = int(input())
            statements.append((s, b))
        possible = []
        for candidate in range(1, n + 1):
            flag = True
            for idx, (s, b) in enumerate(statements, 1):
                if idx == candidate:
                    if b == 1:
                        if candidate in s:
                            flag = False
                            break
                    else:
                        if candidate not in s:
                            flag = False
                            break
                else:
                    if b == 1:
                        if candidate not in s:
                            flag = False
                            break
                    else:
                        if candidate in s:
                            flag = False
                            break
            if flag:
                possible.append(str(candidate))
        if possible:
            answer = ' '.join(possible)
        else:
            answer = 'swi'
        answers.append(f"{answer}")
    print(*answers, sep="\n")