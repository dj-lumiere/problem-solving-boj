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
        K, N = int(input()), int(input())
        rankings = [[int(input()) for _ in range(N)] for _ in range(K)]
        pos = [{} for _ in range(K)]
        for k in range(K):
            for idx, cow in enumerate(rankings[k]):
                pos[k][cow] = idx
        count = 0
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                first = None
                consistent = True
                for k in range(K):
                    if pos[k][i] < pos[k][j]:
                        if first is None:
                            first = 'i'
                        elif first != 'i':
                            consistent = False
                            break
                    else:
                        if first is None:
                            first = 'j'
                        elif first != 'j':
                            consistent = False
                            break
                if consistent:
                    count += 1
        answer = count
        answers.append(f"{answer}")
    print(*answers, sep="\n")