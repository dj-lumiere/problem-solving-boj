# 30992 결혼식이 끝나고

from fractions import Fraction


def find_a_and_b(x1, x2, y1, y2) -> tuple[Fraction, Fraction]:
    return Fraction(y2 - y1, x2 - x1), y1 - x1 * Fraction(y2 - y1, x2 - x1)


result1 = 0
result2 = 0

N = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i, (x2, y2) in enumerate(zip(x, y)):
    if i == 0:
        continue
    x1, y1 = x[i - 1], y[i - 1]
    a, b = find_a_and_b(x1, x2, y1, y2)
    if a == 0:
        result1 += b**4 * (x2 - x1)
        result2 += b**2 * (x2 - x1)
    else:
        result1 += (y2**5 - y1**5) / (5 * a)
        result2 += (y2**3 - y1**3) / (3 * a)

a, b = Fraction(result1, result2).as_integer_ratio()
print(a * pow(b, -1, 998244353) % (998244353))
