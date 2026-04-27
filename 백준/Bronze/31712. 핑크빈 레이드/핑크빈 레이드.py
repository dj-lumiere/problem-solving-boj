cu, du = map(int, input().split())
cd, dd = map(int, input().split())
cp, dp = map(int, input().split())
h = int(input())
max_damage = [0 for _ in range(10001)]
max_damage[0] = du + dd + dp
for i in range(1, 10001):
    max_damage[i] = max_damage[i - 1]
    if not i % cu:
        max_damage[i] += du
    if not i % cd:
        max_damage[i] += dd
    if not i % cp:
        max_damage[i] += dp
for i, v in enumerate(max_damage):
    if v >= h:
        print(i)
        break