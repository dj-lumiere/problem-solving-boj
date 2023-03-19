# 9735 삼차 방정식 풀기
from decimal import Decimal, getcontext

getcontext().prec = 100
T = int(input())
for i in range(T):
    # 계수 로딩
    a, b, c, d = list(map(Decimal, input().split(" ")))
    root_list = []
    if d == 0:
        root_list.append(Decimal(0))
    else:
        for i in range(1, 1000000 + 1):
            if a % i == 0 or d % i == 0:
                if a * i**3 + b * i**2 + c * i + d == 0:
                    root_list.append(Decimal(i))
                    break
                elif a * i**3 - b * i**2 + c * i - d == 0:
                    root_list.append(Decimal(-i))
                    break
    a, b = a, b + a * root_list[-1]
    b, c = b, c + b * root_list[-1]
    c, d = c, d + c * root_list[-1]
    det = b**2 - 4 * a * c
    if det >= 0:
        root_list.append((-b - det.sqrt()) / (2 * a))
        root_list.append((-b + det.sqrt()) / (2 * a))
    root_list = list(set([i.__round__(5) for i in root_list]))
    root_list.sort()
    print(*root_list, sep=" ")