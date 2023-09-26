# 13301 타일 장식물

fib = [0, 1, 1]
for i in range(80):
    fib.append(sum(fib[-2:]))
n = int(input())
print(fib[n + 2] * 2)