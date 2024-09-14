from sys import setrecursionlimit, stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(1, t + 1):
        n, m = int(input()), int(input())
        # 삼각형용 그리드 (상하좌우로 두 칸씩 패딩 필요)
        grid_triangle = [[0 for c in range(n + 2)] for r in range(n + 2)]
        # imos법 사용
        # 삼각형은 6칸만 기록하고 좌우, 상하, 우하향 순으로 누적합
        for _ in range(m):
            b, a, x = (int(input()) + 1 for _ in range(3))
            b -= 2
            a -= 2
            grid_triangle[b][a] += 1
            grid_triangle[b][a + 1] -= 1
            grid_triangle[b + x][a + x + 1] += 1
            grid_triangle[b + x + 1][a + x + 1] -= 1
            grid_triangle[b + x][a] -= 1
            grid_triangle[b + x + 1][a + 1] += 1
        # 좌우
        for y in range(n + 2):
            x = 1
            while is_inbound(x, n + 2, y, n + 2):
                grid_triangle[y][x] += grid_triangle[y][x - 1]
                x += 1
        # 상하
        for x in range(n + 2):
            y = 1
            while is_inbound(x, n + 2, y, n + 2):
                grid_triangle[y][x] += grid_triangle[y - 1][x]
                y += 1
        # 우하향
        for r, dy_minus_dx in enumerate(range(-n - 3, n + 4)):
            if dy_minus_dx < 0:
                x, y = -dy_minus_dx, 0
            else:
                x, y = 0, dy_minus_dx
            x += 1
            y += 1
            while is_inbound(x, n + 2, y, n + 2):
                grid_triangle[y][x] += grid_triangle[y - 1][x - 1]
                x += 1
                y += 1
        answer = sum(sum(bool(v2) for v2 in v) for v in grid_triangle)
        answers.append(f"{answer}")
print(*answers, sep="\n")
