t = int(input())
for _ in range(t):
    c, r = map(int, input().split())
    print(("X"*c+"\n")*r)