k = int(input())
n = int(input())
answer = 0
for i in range(1, n+1):
    a = str(i).replace(str(k), "")
    if not a:
        a="0"
    answer += int(a)
print(answer % (10**9+7))