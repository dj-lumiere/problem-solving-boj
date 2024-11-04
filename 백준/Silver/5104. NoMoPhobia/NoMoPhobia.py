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
    t = INF
    answers = []
    codes = {'TT': 75, 'TX': 50, 'PR': 80, 'RT': 30, 'AP': 25, 'PX': 60}
    for hh in range(t):
        W = int(input())
        N = int(input())
        if W == N == 0:
            break
        points = {}
        order = []
        for _ in range(N):
            name = input()
            code = input()
            if name not in points:
                points[name] = 0
                order.append(name)
            points[name] += codes[code]
        confiscated = [name for name in order if points[name] >= 100]
        if confiscated:
            answer = f"Week {W} " + ",".join(confiscated)
        else:
            answer = f"Week {W} No phones confiscated"
        answers.append(f"{answer}")
    print(*answers, sep="\n")