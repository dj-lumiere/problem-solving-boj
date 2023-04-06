# 26217 별꽃의 세레나데 (Easy)

from decimal import Decimal, getcontext
getcontext().prec = 1000

N: int = int(input())
answer: Decimal = Decimal(0)
for i in range(1, N + 1):
    answer += Decimal(N) / Decimal(i)
print(answer)