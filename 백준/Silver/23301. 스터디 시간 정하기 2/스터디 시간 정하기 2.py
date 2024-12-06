from sys import stderr, stdout


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
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for case in range(1, t + 1):
        N = int(input())
        T = int(input())
        participants = []
        for _ in range(N):
            K = int(input())
            intervals = []
            for _ in range(K):
                S = int(input())
                E = int(input())
                intervals.append((S, E))
            participants.append(intervals)
        max_satisfaction = -1
        best_start = 0
        for start in range(0, 1001 - T + 1):
            end = start + T
            total = 0
            for intervals in participants:
                for S, E in intervals:
                    overlap = max(0, min(E, end) - max(S, start))
                    total += overlap
            if total > max_satisfaction:
                max_satisfaction = total
                best_start = start
        answer = f"{best_start} {best_start + T}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")