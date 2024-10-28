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
    MOD = 1_000_000_009
    t = INF
    answers = []
    for _ in range(t):
        speed, weight, strength = float(input()), float(input()), float(input())
        if speed == 0 and weight == 0 and strength == 0:
            break
        positions = []
        if speed <= 4.5 and weight >= 150 and strength >= 200:
            positions.append("Wide Receiver")
        if speed <= 6.0 and weight >= 300 and strength >= 500:
            positions.append("Lineman")
        if speed <= 5.0 and weight >= 200 and strength >= 300:
            positions.append("Quarterback")
        if positions:
            answer = ' '.join(positions)
        else:
            answer = "No positions"
        answers.append(f"{answer}")
    print(*answers, sep="\n")