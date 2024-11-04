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
        n = int(input())
        strings = [(input(), input()) for _ in range(n)]
        sec = subsec = subsubsec = 0
        for cmd, title in strings:
            if cmd == 'section':
                sec += 1
                subsec = 0
                subsubsec = 0
                numbering = f"{sec} {title}"
            elif cmd == 'subsection':
                subsec += 1
                subsubsec = 0
                numbering = f"{sec}.{subsec} {title}"
            elif cmd == 'subsubsection':
                subsubsec += 1
                numbering = f"{sec}.{subsec}.{subsubsec} {title}"
            answers.append(f"{numbering}")
    print(*answers, sep="\n")