from decimal import Decimal, getcontext

getcontext().prec = 32000

N = input()

print(Decimal(2) ** Decimal(N) if Decimal(2) ** Decimal(N)<Decimal("1e4300") else "")
