from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        s1 = input()
        s2 = input()
        max_overlap = 0
        min_len = min(len(s1), len(s2))
        for i in range(1, min_len + 1):
            if s1[-i:] == s2[:i]:
                if i > max_overlap:
                    max_overlap = i
        for i in range(1, min_len + 1):
            if s2[-i:] == s1[:i]:
                if i > max_overlap:
                    max_overlap = i
        answer = f"{max_overlap}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")