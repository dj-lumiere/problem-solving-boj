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
    for hh in range(t):
        n = int(input())
        k = int(input())
        shared = [int(input()) for _ in range(n)]
        team = [int(input()) for _ in range(n)]
        max_shared = max(shared)
        min_shared = min(shared)
        team_scores = []
        for tj in team:
            if tj >=0:
                max_score = tj * max_shared
            else:
                max_score = tj * min_shared
            team_scores.append(max_score)
        team_scores_sorted = sorted(team_scores, reverse=True)
        if k >= n:
            answer = "-1"
        else:
            answer = f"{team_scores_sorted[k]}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")