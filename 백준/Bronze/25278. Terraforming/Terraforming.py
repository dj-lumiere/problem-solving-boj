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
        n = int(input())
        ocean = 0
        oxygen = 0
        temperature = -30
        for _ in range(n):
            element = input()
            value = int(input())
            if element == 'oxygen':
                oxygen += value
            elif element == 'ocean':
                ocean += value
            elif element == 'temperature':
                temperature += value
        if ocean >= 9 and oxygen >= 14 and temperature >= 8:
            answer = "liveable"
        else:
            answer = "not liveable"
        answers.append(f"{answer}")
    print(*answers, sep="\n")