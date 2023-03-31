# 15682 삼차 방정식 풀기 2
from decimal import Decimal, getcontext
from typing import Callable

getcontext().prec = 90

T = int(input())
for i in range(T):
    # 계수 로딩
    a, b, c, d = list(map(Decimal, input().split(" ")))
    f: Callable[[Decimal], Decimal] = lambda x: a * x**3 + b * x**2 + c * x + d
    f_prime: Callable[[Decimal], Decimal] = lambda x: 3 * a * x**2 + 2 * b * x + c
    root_list: list[Decimal] = []
    if d == 0:
        root_list.append(Decimal(0))
    else:
        x: Decimal = Decimal(0)
        while True:
            next_x = x - f(x) / f_prime(x)
            if abs(next_x - x) <= Decimal("0." + "0" * 30 + "1"):
                root_list.append(x)
                break
            else:
                x = next_x
    a, b = a, b + a * root_list[-1]
    b, c = b, c + b * root_list[-1]
    c, d = c, d + c * root_list[-1]
    det: Decimal = b**2 - 4 * a * c
    if Decimal("-0." + "0" * 30 + "1") < det < Decimal("0"):
        det = Decimal("0")
    if det >= 0:
        root_list.append((-b - det.sqrt()) / (2 * a))
        root_list.append((-b + det.sqrt()) / (2 * a))
    root_list = list(set([i.__round__(10) for i in root_list]))
    root_list.sort()
    root_list_for_answer = [f"{i:.10f}" for i in root_list]
    print(*root_list_for_answer, sep=" ")