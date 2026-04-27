n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
count = {}
for v in grid:
    for v2 in v:
        if v2 not in count:
            count[v2] = 0
        count[v2] += 1
odd_value_count = sum(i%2 for i in count.values())
if odd_value_count <= (n if m%2==1 else 0):
    print("YES")
else:
    print("NO")