from sys import stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(1, t + 1):
        N = int(input())
        names = [input() for _ in range(N)]
        max_unique = -1
        leader = ""
        for name in names:
            unique_letters = set(name.replace(" ", ""))
            count = len(unique_letters)
            if count > max_unique or (count == max_unique and name < leader):
                max_unique = count
                leader = name
        answer = f"Case #{hh}: {leader}"
        answers.append(answer)
    print(*answers, sep="\n")