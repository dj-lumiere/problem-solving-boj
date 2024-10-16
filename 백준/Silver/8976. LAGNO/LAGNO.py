from sys import stderr, stdout

with open(0, "r") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_007
    x = 1
    answers = []
    for hh in range(1, x + 1):
        board = [input() for _ in range(8)]


        def count_flips(r, c, dr, dc):
            flips, y, x = 0, r + dr, c + dc
            while is_inbound(x, 8, y, 8) and board[y][x] == 'W':
                flips, y, x = flips + 1, y + dr, x + dc
            return flips if is_inbound(x, 8, y, 8) and board[y][x] == 'B' else 0


        answer = max(sum(count_flips(r, c, dr, dc) for dr, dc in DELTA) for r in range(8) for c in range(8) if
                     board[r][c] == '.')
        answers.append(f"{answer}")
    print(*answers, sep="\n")