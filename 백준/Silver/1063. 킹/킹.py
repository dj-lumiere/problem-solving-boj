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
    for hh in range(t):
        directions = {
            "R" : (1, 0), "L": (-1, 0), "B": (0, -1), "T": (0, 1),
            "RT": (1, 1), "LT": (-1, 1), "RB": (1, -1), "LB": (-1, -1)
        }
        king_pos = input()
        stone_pos = input()
        n = int(input())
        king_x, king_y = ord(king_pos[0]) - ord('A'), int(king_pos[1]) - 1
        stone_x, stone_y = ord(stone_pos[0]) - ord('A'), int(stone_pos[1]) - 1
        for _ in range(n):
            move = input()
            dx, dy = directions[move]
            new_king_x, new_king_y = king_x + dx, king_y + dy
            if 0 <= new_king_x < 8 and 0 <= new_king_y < 8:
                if new_king_x == stone_x and new_king_y == stone_y:
                    new_stone_x, new_stone_y = stone_x + dx, stone_y + dy
                    if 0 <= new_stone_x < 8 and 0 <= new_stone_y < 8:
                        king_x, king_y, stone_x, stone_y = new_king_x, new_king_y, new_stone_x, new_stone_y
                else:
                    king_x, king_y = new_king_x, new_king_y
        final_king_pos = f"{chr(king_x + ord('A'))}{king_y + 1}"
        final_stone_pos = f"{chr(stone_x + ord('A'))}{stone_y + 1}"
        answers.extend([final_king_pos, final_stone_pos])
    print(*answers, sep="\n")