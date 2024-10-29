from bisect import bisect_left, bisect_right
from sys import stdout, stderr

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
    for hh in range(t):
        current_game = []
        while True:
            token = input()
            if token is None:
                break
            if token == '#':
                t = hh
                break
            if token == '*':
                break
            current_game.append(token)
        if token == '#':
            break
        cheryl = 0
        tania = 0
        for card in current_game:
            if card == 'A':
                value = 1
            else:
                value = int(card)
            if value % 2 == 1:
                cheryl += 1
            else:
                tania += 1
        if cheryl > tania:
            answer = 'Cheryl'
        elif tania > cheryl:
            answer = 'Tania'
        else:
            answer = 'Draw'
        answers.append(f"{answer}")
    print(*answers, sep="\n")