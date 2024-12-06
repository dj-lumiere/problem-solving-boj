from sys import stderr, stdout


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
    rprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    erprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(repr, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    frprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(repr, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = int(input())
    answers = []
    for hh in range(1, t+1):
        A = int(input())
        security_answers = [input() for _ in range(A)]
        L = int(input())
        attempts = [input() for _ in range(L)]
        results = []
        for attempt in attempts:
            parts = attempt.split()
            answer_num = int(parts[0]) - 1
            pos1 = int(parts[1])
            pos2 = int(parts[2])
            entered1 = parts[3]
            entered2 = parts[4]
            answer = security_answers[answer_num]
            letters = ''.join([ch for ch in answer if ch != ' '])
            if pos1 <= len(letters) and pos2 <= len(letters):
                correct1 = letters[pos1 - 1]
                correct2 = letters[pos2 - 1]
                if entered1 == correct1 and entered2 == correct2:
                    results.append("correct")
                else:
                    results.append("error")
            else:
                results.append("error")
        answers.append(f"Customer {hh}")
        for res in results:
            answers.append(f"{res}")
    print(*answers, sep="\n")