from decimal import getcontext
from sys import stderr, stdout

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
        N, Q, K = int(input()), int(input()), int(input())
        A = [int(input()) for _ in range(N)]
        swap_count = 0
        answer = -1
        stack = [(0, N - 1, Q)]
        while stack:
            p, r, q = stack.pop()
            if p == r:
                continue
            x = A[r]
            i = p - 1
            for j in range(p, r):
                if A[j] <= x:
                    i += 1
                    A[i], A[j] = A[j], A[i]
                    swap_count += 1
                    if swap_count == K:
                        answer = f"{min(A[i], A[j])} {max(A[i], A[j])}"
                        break
            if swap_count == K:
                break
            if i + 1 != r:
                A[i + 1], A[r] = A[r], A[i + 1]
                swap_count += 1
                if swap_count == K:
                    answer = f"{min(A[i + 1], A[r])} {max(A[i + 1], A[r])}"
                    break
            t_pos = i + 1
            k_val = t_pos - p + 1
            if q < k_val:
                stack.append((p, t_pos - 1, q))
            elif q > k_val:
                stack.append((t_pos + 1, r, q - k_val))
        answers.append(str(answer))
    print(*answers, sep="\n")