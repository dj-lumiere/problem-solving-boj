n = int(input())
tb = [list(map(int, input().split())) for _ in range(n)]
t_max = max(x[0] for x in tb)
b_min = min(x[1] for x in tb)
print(t_max * b_min % 7 + 1)