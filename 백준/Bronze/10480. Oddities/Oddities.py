# 10480 Oddities

N = int(input())
for _ in range(N):
    x = int(input())
    oddity = x % 2
    print(f"{x} is odd" if oddity else f"{x} is even")