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
    for _ in range(t):
        initial_time = input()
        hh, mm = map(int, initial_time.split(':'))
        ppf_values = [int(input()) for _ in range(6)]
        L = int(input())
        events = []
        for _ in range(L):
            s_T = input()
            action = input()
            s, T = s_T.split('.')
            t_event = int(s) + int(T) * 1e-3
            events.append((t_event, action))
        sealed_regions = set()
        items_added_time = 0.0
        last_event_time = 0.0
        t_end = 60.0
        for event in events:
            t_event, action = event
            if t_event > 60.0:
                break
            clock_time_sec = (hh * 3600 + mm * 60 + t_event + items_added_time) % 43200
            region_num = int(clock_time_sec // 7200) + 1
            if action == '^':
                sealed_regions.add(region_num)
                if len(sealed_regions) == 6:
                    t_end = t_event
                    break
            else:
                if action == "10MIN":
                    items_added_time += 600
                elif action == "30MIN":
                    items_added_time += 1800
                elif action == "50MIN":
                    items_added_time += 3000
                elif action == "2HOUR":
                    items_added_time += 7200
                elif action == "4HOUR":
                    items_added_time += 14400
                elif action == "9HOUR":
                    items_added_time += 32400
            last_event_time = t_event
        if len(sealed_regions) < 6:
            t_end = 60.0
        sum_unsealed = sum(ppf_values[i - 1] for i in range(1, 7) if i not in sealed_regions)
        h = int(min(sum_unsealed, 100))
        answer = h
        answers.append(f"{answer}")
    print(*answers, sep="\n")