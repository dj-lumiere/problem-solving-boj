n=int(input())
x, s=map(int, input().split())
answer=False
for _ in range(n):
    c, p = map(int, input().split())
    if c <= x and p>s: answer=True
print("YES" if answer else "NO")