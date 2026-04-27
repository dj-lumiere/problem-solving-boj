l = int(input())
n = int(input())
pk = [list(map(int, input().split())) for _ in range(n)]
cake = [0 for _ in range(l+1)]
for i, (p, k) in enumerate(pk, start=1):
    for j in range(p, k+1):
        if cake[j]: continue
        cake[j] = i
max_piece = 0
min_number = n+1
for i in reversed(range(1, n+1)):
    if max_piece < cake.count(i):
        max_piece = cake.count(i)
        min_number = i
    elif max_piece == cake.count(i):
        min_number = i
expected_max_piece = 0
expected_min_number = n+1
for i in reversed(range(1, n+1)):
    p,k = pk[i-1]
    if expected_max_piece < k-p+1:
        expected_max_piece = k-p+1
        expected_min_number = i
    elif expected_max_piece == k-p+1:
        expected_min_number = i
print(f"{expected_min_number}\n{min_number}")