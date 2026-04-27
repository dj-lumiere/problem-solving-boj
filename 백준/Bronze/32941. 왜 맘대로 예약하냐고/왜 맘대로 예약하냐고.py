t, x = map(int, input().split())
k = []
n = int(input())
for _ in range(n):
    _ = int(input())
    k.append(set(map(int, input().split())))
print("YES" if all(x in v for v in k) else "NO")