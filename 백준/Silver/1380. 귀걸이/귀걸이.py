from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
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
    for hh in range(t):
        n = int(input())
        if n == 0:
            break
        names = [input() for _ in range(n)]
        counts = {i + 1: 0 for i in range(n)}
        for _ in range(2 * n - 1):
            num, ab = input().split()
            counts[int(num)] += 1
        no_earring = []
        for i in counts:
            if counts[i] < 2:
                no_earring.append(names[i - 1])
                break
        answer = f"{hh + 1} " + " ".join(no_earring)
        answers.append(f"{answer}")
    print(*answers, sep="\n")