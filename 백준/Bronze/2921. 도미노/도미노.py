# 3921 도미노

n = int(input())
answer = (
    sum(i for i in range(n + 1)) * 2 * (n + 1) + 2 * sum(i for i in range(n + 1))
) // 2
print(answer)