from sys import stderr, stdout

with open(0, 'r') as f:
    tokens = iter(f.read().split())
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
        n, m = int(input()), int(input())
        grid = [input() for _ in range(n)]
        row_counts = []
        for row in grid:
            counts = []
            count = 0
            for c in row:
                if c == '#':
                    count += 1
                else:
                    if count > 0:
                        counts.append(str(count))
                        count = 0
            if count > 0:
                counts.append(str(count))
            row_counts.append(' '.join(counts) if counts else '0')
        col_counts = []
        for col in range(m):
            counts = []
            count = 0
            for row in range(n):
                if grid[row][col] == '#':
                    count += 1
                else:
                    if count > 0:
                        counts.append(str(count))
                        count = 0
            if count > 0:
                counts.append(str(count))
            col_counts.append(' '.join(counts) if counts else '0')
        answer = '\n'.join(row_counts + col_counts)
        answers.append(f"{answer}")
    print(*answers, sep="\n")