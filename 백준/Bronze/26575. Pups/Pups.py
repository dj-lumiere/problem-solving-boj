# 26575 Pups


def my_round_function(number: float, digit: int):
    x = int(number * (10 ** (digit + 1)))
    int_part, frac_part = divmod(x, 10 ** (digit + 1))
    frac_part, rounding_part_check = divmod(frac_part, 10)
    if rounding_part_check >= 5:
        frac_part += 1
    return f"{int_part}.{str(frac_part).zfill(digit)}"


n = int(input())
for _ in range(n):
    d, f, p = map(float, input().split(" "))
    print("$" + my_round_function(d * f * p, 2))