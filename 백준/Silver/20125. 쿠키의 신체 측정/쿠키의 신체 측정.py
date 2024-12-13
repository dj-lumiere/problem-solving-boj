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
    t = INF
    answers = []
    for hh in range(t):
        n_token = input()
        if n_token is None:
            break
        n = int(n_token)
        grid = []
        for _ in range(n):
            row = input()
            grid.append(row)
        heart_x, heart_y = -1, -1
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                if grid[i][j] == '*' and grid[i - 1][j] == '*' and grid[i + 1][j] == '*' and grid[i][j - 1] == '*' and \
                        grid[i][j + 1] == '*':
                    heart_x, heart_y = i, j
                    break
            if heart_x != -1:
                break
        la = 0
        j = heart_y - 1
        while j >= 0 and grid[heart_x][j] == '*':
            la += 1
            j -= 1
        ra = 0
        j = heart_y + 1
        while j < n and grid[heart_x][j] == '*':
            ra += 1
            j += 1
        wa = 0
        i_pos = heart_x + 1
        while i_pos < n and grid[i_pos][heart_y] == '*':
            wa += 1
            i_pos += 1
        wa_end_x, wa_end_y = heart_x + wa, heart_y
        left_leg = 0
        li = wa_end_x + 1
        lj = wa_end_y - 1
        while li < n and grid[li][lj] == '*':
            left_leg += 1
            li += 1
        right_leg = 0
        ri = wa_end_x + 1
        rj = wa_end_y + 1
        while ri < n and grid[ri][rj] == '*':
            right_leg += 1
            ri += 1
        answer = f"{heart_x + 1} {heart_y + 1}\n{la} {ra} {wa} {left_leg} {right_leg}"
        answers.append(answer)
    print(*answers, sep="\n")