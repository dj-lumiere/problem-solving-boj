t = int(input())
for i in range(1, t+1):
    n, b = map(int, input().split())
    h = list(map(int, input().split()))
    tower_height = lambda mask, h: sum((mask & (1<<i) != 0)*v for i,v in enumerate(h))
    print(f"#{i} {min(tower_height(mask, h)-b for mask in range(1, 1<<n) if tower_height(mask, h) >= b)}")