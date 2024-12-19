# 21967번 세워라 반석 위에
from decimal import Decimal, getcontext
from fractions import Fraction
from sys import stdout, stderr

getcontext().prec = 30


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        A = [int(input()) for _ in range(n)]
        counts = [0] * 11
        counts[A[0]] += 1
        max_val = A[0]
        min_val = A[0]
        left = 0
        max_len = 1
        for right in range(1, n):
            counts[A[right]] += 1
            if A[right] > max_val:
                max_val = A[right]
            if A[right] < min_val:
                min_val = A[right]
            while max_val - min_val > 2:
                counts[A[left]] -= 1
                if counts[A[left]] == 0:
                    if A[left] == max_val:
                        for i in range(max_val - 1, 0, -1):
                            if counts[i] > 0:
                                max_val = i
                                break
                    if A[left] == min_val:
                        for i in range(min_val + 1, 11):
                            if counts[i] > 0:
                                min_val = i
                                break
                left += 1
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
        answer = max_len
        answers.append(f"{answer}")
    print(*answers, sep="\n")