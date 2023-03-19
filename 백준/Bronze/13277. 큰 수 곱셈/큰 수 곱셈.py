from decimal import Decimal, getcontext
getcontext().prec = 600000

a, b = list(map(Decimal, input().split(" ")))
print(a * b)