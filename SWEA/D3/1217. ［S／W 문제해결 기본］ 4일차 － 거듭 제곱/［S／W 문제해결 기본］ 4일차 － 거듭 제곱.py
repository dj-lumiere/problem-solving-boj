t = 10
for _ in range(t):
    a = int(input())
    x, y = map(int, input().split())
    print(f"#{a} {pow(x, y)}")