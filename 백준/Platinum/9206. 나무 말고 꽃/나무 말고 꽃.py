# 9206 나무 말고 꽃

from decimal import Decimal, getcontext

getcontext().prec = 150

# integral exp(-2x^2)+2absqrt(x)exp(-x^2)+b^2x


def integral_exp_minus_2x_square(x: Decimal):
    coefficient = Decimal(1)
    dimension = 0
    answer = Decimal(0)
    while True:
        if dimension == 0:
            dx = x
            answer += dx
            dimension += 1
        else:
            dx = (
                dx
                * (-2 * x * x)
                / Decimal(dimension)
                * Decimal(2 * dimension - 1)
                / Decimal(2 * dimension + 1)
            )
            answer += dx
            dimension += 1
        if abs(dx) < Decimal("1e-40"):
            break
    return answer


def integral_sqrt_x_times_exp_minus_x_square(x: Decimal):
    coefficient = Decimal(1)
    dimension = 0
    answer = Decimal(0)
    while True:
        if dimension == 0:
            dx = x * x.sqrt() / Decimal("1.5")
            answer += dx
            dimension += 1
        else:
            dx = (
                dx
                * (-x * x)
                / Decimal(dimension)
                * Decimal(4 * dimension - 1)
                / Decimal(4 * (dimension + 1) - 1)
            )
            answer += dx
            dimension += 1
        if abs(dx) < Decimal("1e-40"):
            break
    return answer


pi = Decimal("3.141592653589793238462643383279502884197169399375105820974944")
V, N = map(Decimal, input().split(" "))
vase_volume_difference_list = []
for _ in range(int(N)):
    a, b, h = map(Decimal, input().split(" "))
    vase_volume = (
        a * a * integral_exp_minus_2x_square(h)
        + 2 * a * b * integral_sqrt_x_times_exp_minus_x_square(h)
        + b * b * h * h / 2
    ) * pi
    vase_volume_difference_list.append(abs(V - vase_volume))
minimum_difference = Decimal("1e10")
index = 0
for (i, j) in enumerate(vase_volume_difference_list):
    if minimum_difference > j:
        minimum_difference = j
        index = i
print(index)