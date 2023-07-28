# 16428 A/B - 3

a, b = map(int, input().split(" "))
quotient, remainder = divmod(a, b)
if b < 0 and remainder != 0:
    quotient += 1
    remainder -= b
print(quotient, remainder, sep="\n")