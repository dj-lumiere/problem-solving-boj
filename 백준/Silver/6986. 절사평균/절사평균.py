from sys import stderr, stdout


def precise_round(numerator: int, denominator: int, precision: int) -> str:
    scaling_factor = 10 ** precision
    raw_value = numerator * scaling_factor * 10 // denominator
    rounded_value = (raw_value + 5) // 10
    integer_part, fractional_part = divmod(rounded_value, scaling_factor)
    return f"{integer_part}.{str(fractional_part).zfill(precision)}"


with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = 1
    answers = []
    for hh in range(t):
        n, k = int(input()), int(input())
        scores = [int(float(input()) * 10) for _ in range(n)]
        scores.sort()
        trimmed = scores[k:n - k]
        trimmed_mean = precise_round(sum(trimmed), (n - 2 * k) * 10, 2)
        adjusted = [scores[k]] * k + trimmed + [scores[n - k - 1]] * k
        adjusted_mean = precise_round(sum(adjusted), n * 10, 2)
        answer = f"{trimmed_mean}\n{adjusted_mean}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")