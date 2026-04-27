n, m = map(int, input().split())
count = {}
for _ in range(n):
    x = int(input())
    ids = list(map(int, input().split()))
    for i in ids:
        if i not in count:
            count[i] = 0
        count[i] += 1
print(sum(v>=m for v in count.values()))