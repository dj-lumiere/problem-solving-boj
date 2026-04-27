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
    for _ in range(t):
        N = int(input())
        chairs = list(range(1, N+1))
        chairs[0] = None
        moved = set()
        current_cow = 1
        last_cow = None
        while True:
            current_index = current_cow -1
            move_steps = current_cow
            target_index = (current_index + move_steps) % N
            target_cow = chairs[target_index]
            if target_cow is None:
                last_cow = current_cow
                break
            if target_cow in moved:
                last_cow = current_cow
                break
            chairs[target_index] = current_cow
            chairs[current_index] = None
            moved.add(target_cow)
            current_cow = target_cow
        answer = last_cow
        answers.append(f"{answer}")
    print(*answers, sep="\n")