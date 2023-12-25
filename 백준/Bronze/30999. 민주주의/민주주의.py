# 30999 민주주의

N, M = map(int, input().split())
result = 0
for _ in range(N):
    votes = list(input())
    result += sum([i == "O" for i in votes]) * 2 >= M
print(result)