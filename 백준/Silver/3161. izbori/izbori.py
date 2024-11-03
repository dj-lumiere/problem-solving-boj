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
        M = int(input())
        N = int(input())
        ballots = [list(map(int, [input() for _ in range(N)])) for _ in range(M)]
        rank = []
        for ballot in ballots:
            pos = {}
            for idx, candidate in enumerate(ballot):
                pos[candidate] = idx
            rank.append(pos)
        scores = [0] * (N + 1)
        for A in range(1, N + 1):
            for B in range(1, N + 1):
                if A == B:
                    continue
                count = sum(1 for r in rank if r[A] < r[B])
                if count > M // 2:
                    scores[A] += 1
        max_score = max(scores[1:])
        winners = [str(i) for i in range(1, N + 1) if scores[i] == max_score]
        answer = '\n'.join(winners)
        answers.append(f"{answer}")
    print(*answers, sep="\n")