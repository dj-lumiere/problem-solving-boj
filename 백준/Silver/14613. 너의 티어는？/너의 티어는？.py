# 14613 너의 티어는?

from decimal import Decimal, getcontext
from math import factorial
getcontext().prec = 40

# 1000 : W-L = -20
# 1500 : W-L = -10
# 2000 : W-L = 0
# 2500 : W-L = 10
# 3000 : W-L = 20

percent = lambda x: int(Decimal(x) * 100)
W, L, D = list(map(percent, input().split(" ")))


def nCr(n, r) -> int:
    return factorial(n) // (factorial(r) * factorial(n - r))


def multinomial_coefficient(A: int, B: int, C: int) -> int:
    value = (
        nCr(20, A) * nCr(20 - A, B) * nCr(20 - A - B, C)
    )
    return value

wins_possibility = [0 for i in range(40 + 1)]

for w in range(20 + 1):
    for l in range(20 - w + 1):
        wins_possibility[w-l+20] += (
            multinomial_coefficient(w, l, 20 - w - l)
            * (W ** w)
            * (L ** l)
            * (D ** (20 - w - l))
        )

wins_possibility = [(Decimal(i) / Decimal(10**40)) for i in wins_possibility]
tier_possibility = [sum(wins_possibility[10*i:min(40+1,10*(i+1))]) for i in range(4+1)]

getcontext().prec = 8
truncation = lambda x: f"{Decimal(x):.8f}"
print("\n".join(map(truncation, tier_possibility)))