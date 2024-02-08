# 1964 오각형, 오각형, 오각형…

N = int(input())
answer = 5
for i in range(2, N + 1):
    answer += 3 * i + 1
    answer %= 45678
print(answer)