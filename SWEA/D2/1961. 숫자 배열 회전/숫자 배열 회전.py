def spin(grid, size):
    return [[grid[size-x-1][y] for x in range(size)] for y in range(size)]

t = int(input())
for i in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    grid2 = spin(grid, n)
    grid3 = spin(grid2, n)
    grid4 = spin(grid3, n)
    print(f"#{i+1}")
    print("\n".join(f"{''.join(map(str, a))} {''.join(map(str, b))} {''.join(map(str, c))}" for a, b, c, in zip(grid2, grid3, grid4)))