n = int(input())
logo = [[" " for _ in range(4*n+2)] for _ in range(2*n)]
start_up_x = [0, n, 2*n+1, 3*n+2]
start_up_y = [2*n-1, n-1, n-1, 2*n-1]
start_down_x = [2*n+1, 3*n+2]
start_down_y = [n, 0]
for i in range(n):
    for x, y in zip(start_up_x, start_up_y):
        logo[y-i][x+i] = "*"
    for x, y in zip(start_down_x, start_down_y):
        logo[y+i][x+i] = "*"
print("\n".join("".join(x) for x in logo))