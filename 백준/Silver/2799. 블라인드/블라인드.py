from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        m, n = map(int, input().split())
        grid = [input() for _ in range(5 * m + 1)]
        patterns = [["....", "....", "....", "...."], ["****", "....", "....", "...."],
                    ["****", "****", "....", "...."], ["****", "****", "****", "...."],
                    ["****", "****", "****", "****"]]
        counts = [0] * 5
        for floor in range(m):
            for window in range(n):
                window_grid = [grid[5 * floor + i + 1][5 * window + 1:5 * window + 5] for i in range(4)]
                eprint(window_grid)
                for idx, pattern in enumerate(patterns):
                    if window_grid == pattern:
                        counts[idx] += 1
                        break
        answer = ' '.join(map(str, counts))
        answers.append(f"{answer}")
    print(*answers, sep="\n")