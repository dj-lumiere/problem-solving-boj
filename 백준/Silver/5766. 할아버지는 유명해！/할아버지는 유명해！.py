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
    t = INF
    answers = []
    for hh in range(t):
        n = int(input())
        m = int(input())
        if n == 0 and m == 0:
            break
        counts = {}
        for _ in range(n):
            for _ in range(m):
                p = int(input())
                counts[p] = counts.get(p, 0) + 1
        max_point = max(counts.values())
        second_max = max(v for v in counts.values() if v < max_point)
        second_players = sorted([p for p, v in counts.items() if v == second_max])
        answer = ' '.join(map(str, second_players))
        answers.append(f"{answer}")
    print(*answers, sep="\n")