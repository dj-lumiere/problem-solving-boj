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
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(t):
        n = int(input())
        strings = [input() for _ in range(n)]
        k = len(strings[0])
        active = set(range(n))
        for i in range(k):
            moves = [strings[j][i] for j in active]
            unique_moves = set(moves)
            if len(unique_moves) == 1:
                continue
            if 'R' in unique_moves and 'S' in unique_moves and 'P' not in unique_moves:
                losing_move = 'S'
            elif 'S' in unique_moves and 'P' in unique_moves and 'R' not in unique_moves:
                losing_move = 'P'
            elif 'P' in unique_moves and 'R' in unique_moves and 'S' not in unique_moves:
                losing_move = 'R'
            else:
                continue
            to_eliminate = set()
            for j in active:
                if strings[j][i] == losing_move:
                    to_eliminate.add(j)
            active -= to_eliminate
            if len(active) == 1:
                break
        if len(active) == 1:
            winner = list(active)[0] + 1
        else:
            winner = 0
        answer = winner
        answers.append(f"{answer}")
    print(*answers, sep="\n")