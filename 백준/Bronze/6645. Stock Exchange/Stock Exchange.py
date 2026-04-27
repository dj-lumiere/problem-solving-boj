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
    tokens = iter(f.read().splitlines())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = INF
    answers = []
    for hh in range(t):
        first_line = input()
        if first_line == "0 END":
            break
        parts = first_line.split()
        if len(parts) < 2:
            continue
        n = int(parts[0])
        code = parts[1]
        bids = []
        buys = []
        sells = []
        for _ in range(n):
            bid_line = input()
            bid_parts = bid_line.split()
            name = bid_parts[0]
            bid_type = bid_parts[1]
            price = Decimal(bid_parts[2])
            bids.append((name, bid_type, price))
            if bid_type == "buy":
                buys.append((name, price))
            else:
                sells.append((name, price))
        output = [code]
        for name, bid_type, price in bids:
            if bid_type == "buy":
                matches = [s_name for s_name, s_price in sells if s_price <= price]
            else:
                matches = [b_name for b_name, b_price in buys if b_price >= price]
            if matches:
                match_str = ' '.join(matches)
            else:
                match_str = "NO-ONE"
            output.append(f"{name}: {match_str}")
        answer = '\n'.join(output)
        answers.append(answer)
    print(*answers, sep="\n")