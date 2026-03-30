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
    t = 1
    answers = []
    for hh in range(1, t + 1):
        pattern = [".#########",
                   "#.########",
                   "##.#######",
                   "###.######",
                   "####.#####",
                   "#####.####",
                   "######.###",
                   "#######.##",
                   "########.#",
                   "#########.",
                   "########.#",
                   "#######.##",
                   "######.###",
                   "#####.####",
                   "####.#####",
                   "###.######",
                   "##.#######",
                   "#.########",
                   ".#########"]
        pattern = pattern[::-1]
        board = [input() for _ in range(20)]
        board = board[::-1]
        answer = 0
        if pattern[:19] == board[:19] and board[19][0] != ".":
            answer = "GM"
        elif pattern[:18] == board[:18] and board[18][1] != ".":
            answer = "S9"
        elif pattern[:17] == board[:17] and board[17][2] != ".":
            answer = "S8"
        elif pattern[:16] == board[:16] and board[16][3] != ".":
            answer = "S7"
        elif pattern[:15] == board[:15] and board[15][4] != ".":
            answer = "S6"
        elif pattern[:14] == board[:14] and board[14][5] != ".":
            answer = "S5"
        elif pattern[:13] == board[:13] and board[13][6] != ".":
            answer = "S4"
        elif pattern[:12] == board[:12] and board[12][7] != ".":
            answer = "S3"
        elif pattern[:11] == board[:11] and board[11][8] != ".":
            answer = "S2"
        elif pattern[:10] == board[:10] and board[10][9] != ".":
            answer = "S1"
        elif pattern[:9] == board[:9] and board[9][8] != ".":
            answer = "1"
        elif pattern[:8] == board[:8] and board[8][7] != ".":
            answer = "2"
        elif pattern[:7] == board[:7] and board[7][6] != ".":
            answer = "3"
        elif pattern[:6] == board[:6] and board[6][5] != ".":
            answer = "4"
        elif pattern[:5] == board[:5] and board[5][4] != ".":
            answer = "5"
        elif pattern[:4] == board[:4] and board[4][3] != ".":
            answer = "6"
        elif pattern[:3] == board[:3] and board[3][2] != ".":
            answer = "7"
        elif pattern[:2] == board[:2] and board[2][1] != ".":
            answer = "8"
        elif pattern[:1] == board[:1] and board[1][0] != ".":
            answer = "9"
        elif pattern[0] != board[0] or (pattern[0] == board[0] and board[1][0] == "."):
            answer = "X"
        answers.append(answer)
    print(*answers, sep="\n")