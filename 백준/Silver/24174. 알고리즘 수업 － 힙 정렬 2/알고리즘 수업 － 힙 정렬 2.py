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
        k = int(input())
        A = [0] + [int(input()) for _ in range(n)]
        swap_count = 0
        answer = -1
        found = False
        for i in range(n // 2, 0, -1):
            current = i
            while True:
                left = 2 * current
                right = 2 * current + 1
                smaller = current
                if left <= n and A[left] < A[smaller]:
                    smaller = left
                if right <= n and A[right] < A[smaller]:
                    smaller = right
                if smaller != current:
                    A[current], A[smaller] = A[smaller], A[current]
                    swap_count += 1
                    if swap_count == k:
                        answer = ' '.join(map(str, A[1:]))
                        found = True
                        break
                    current = smaller
                else:
                    break
            if found:
                break
        if not found:
            for i in range(n, 1, -1):
                A[1], A[i] = A[i], A[1]
                swap_count += 1
                if swap_count == k:
                    answer = ' '.join(map(str, A[1:]))
                    found = True
                    break
                heap_size = i - 1
                current = 1
                while True:
                    left = 2 * current
                    right = 2 * current + 1
                    smaller = current
                    if left <= heap_size and A[left] < A[smaller]:
                        smaller = left
                    if right <= heap_size and A[right] < A[smaller]:
                        smaller = right
                    if smaller != current:
                        A[current], A[smaller] = A[smaller], A[current]
                        swap_count += 1
                        if swap_count == k:
                            answer = ' '.join(map(str, A[1:]))
                            found = True
                            break
                        current = smaller
                    else:
                        break
                if found:
                    break
        if not found and swap_count < k:
            answer = '-1'
        answers.append(f"{answer}")
    print(*answers, sep="\n")