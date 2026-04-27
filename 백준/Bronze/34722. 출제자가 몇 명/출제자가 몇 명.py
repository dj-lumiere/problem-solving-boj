n = int(input())
answer = 0
for _ in range(n):
    a,b,c,d = map(int, input().split())
    if a >= 1000 or b >= 1600 or c >= 1500 or (d != -1 and d <= 30):
        answer += 1
print(answer)