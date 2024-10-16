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
    x = int(input())
    answers = []
    for hh in range(1, x + 1):
        r, c, msg = int(input()), int(input()), input()
        grid = ["0" for _ in range(r * c)]
        visited = [[False for _ in range(c)] for _ in range(r)]
        di = 0
        x, y = 0, 0
        for idx in range(r * c):
            dx, dy = DELTA[di]
            grid[idx] = msg[y * c + x]
            visited[y][x] = True
            if not is_inbound(y + dy, r, x + dx, c) or visited[y + dy][x + dx]:
                di = (di + 1) % 4
                dx, dy = DELTA[di]
            x, y = x + dx, y + dy
        chars = []
        for j in range(0, r * c, 5):
            digit = int("".join(grid[j:j + 5]), 2)
            if digit:
                chars.append(chr(digit - 1 + ord("A")))
            else:
                chars.append(" ")
        answer = "".join(chars).rstrip()
        answers.append(answer)
    print(*answers, sep="\n")