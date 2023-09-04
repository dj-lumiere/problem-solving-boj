# 9610 사분면

n = int(input())
axis = 0
quarters = [0, 0, 0, 0, 0]
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        axis += 1
    if x > 0 and y > 0:
        quarters[1] += 1
    if x < 0 and y > 0:
        quarters[2] += 1
    if x < 0 and y < 0:
        quarters[3] += 1
    if x > 0 and y < 0:
        quarters[4] += 1
for i in range(1, 5):
    print(f"Q{i}: {quarters[i]}")
print(f"AXIS: {axis}")
