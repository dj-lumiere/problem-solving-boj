# 10610 30

digits = list(map(int, list(input())))
if not (sum(digits) % 3 == 0 and 0 in digits):
    print(-1)
else:
    digits.sort()
    digits.reverse()
    print(*digits, sep="")