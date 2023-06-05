# 28202 Classical A+B Problem
from sys import stdin, stdout
from decimal import Decimal, getcontext

getcontext().prec = 4000
input = stdin.readline
print = stdout.write


def find_digit(n: Decimal) -> int:
    n_as_tuple = n.as_tuple()
    return len(n_as_tuple[1])


T = int(input())
for _ in range(T):
    n = Decimal(input())
    digit = find_digit(n)
    case_found = False
    for i in range(digit, 1 - 1, -1):
        for j in range(9, 1 - 1, -1):
            compare = Decimal(str(j) * i)
            result = n - compare
            result_digit = result.as_tuple()[1]
            if result <= 0:
                continue
            elif all(
                result_digit[k] == result_digit[0] for k in range(find_digit(result))
            ):
                print(f"{compare} {result}\n")
                case_found = True
                break
        if case_found:
            break
