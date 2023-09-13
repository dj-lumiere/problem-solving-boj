# 14782 Bedtime Reading, I

I = int(input())
result = 0
for i in range(1, int(I**0.5) + 1):
    if I % i == 0:
        result += i + I // i
print(result)