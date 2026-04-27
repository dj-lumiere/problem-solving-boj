n, m = map(int, input().split())
grid = [input() for _ in range(n)]
grid_len=min(n,m)
answer=[0]*(grid_len+1)
for i in range(1, grid_len+1):
    for y in range(n-i+1):
        for x in range(m-i+1):
            satisfied = True
            for y2 in range(i):
                for x2 in range(i):
                    if x2==y2 and grid[y+y2][x+x2]!="X":
                        satisfied=False
                    if x2!=y2 and grid[y+y2][x+x2]!=".":
                        satisfied=False
            answer[i] += satisfied
print(*answer[1:], sep="\n")