def is_inbound(x_pos, x_size, y_pos, y_size):
    return 0<=x_pos<x_size and 0<=y_pos<y_size

t=int(input())
for a in range(1, t+1):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    plus_shoot = [[0 for _ in range(n)] for _ in range(n)]
    cross_shoot = [[0 for _ in range(n)] for _ in range(n)]
    for y, v in enumerate(grid):
        for x, v2 in enumerate(v):
            plus_shoot[y][x] += v2
            cross_shoot[y][x] += v2
            for i in range(1, m):
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x+i*dx, y+i*dy
                    if not is_inbound(nx, n, ny, n):
                        continue
                    plus_shoot[y][x] += grid[ny][nx]
                for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
                    nx, ny = x+i*dx, y+i*dy
                    if not is_inbound(nx, n, ny, n):
                        continue
                    cross_shoot[y][x] += grid[ny][nx]
    print(f"#{a} {max(*map(max, plus_shoot), *map(max, cross_shoot))}")