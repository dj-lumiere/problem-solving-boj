from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
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
        swaps = input()
        position = 1
        for move in swaps:
            if move == 'A':
                if position == 1:
                    position = 2
                elif position == 2:
                    position = 1
            elif move == 'B':
                if position == 2:
                    position = 3
                elif position == 3:
                    position = 2
            elif move == 'C':
                if position == 1:
                    position = 3
                elif position == 3:
                    position = 1
        answer = f"{position}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")