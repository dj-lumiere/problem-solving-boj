from sys import stderr, stdout

with open(0, 'r') as f:
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
        time_str = input()
        N = int(input())
        hh_val, mm_val = map(int, time_str.split(':'))
        count = 0
        current_hh = hh_val
        current_mm = mm_val
        if current_mm == 0:
            cuckoos = current_hh if current_hh != 0 else 12
            count += cuckoos
        elif current_mm in [15, 30, 45]:
            count += 1
        if count >= N:
            answer = f"{hh_val:02d}:{mm_val:02d}"
            answers.append(f"{answer}")
        else:
            while count < N:
                current_mm += 1
                if current_mm == 60:
                    current_mm = 0
                    current_hh += 1
                    if current_hh == 13:
                        current_hh = 1
                cuckoos = 0
                if current_mm == 0:
                    cuckoos = current_hh if current_hh != 0 else 12
                elif current_mm in [15, 30, 45]:
                    cuckoos = 1
                count += cuckoos
                if count >= N:
                    answer = f"{current_hh:02d}:{current_mm:02d}"
                    break
            answers.append(f"{answer}")
    print(*answers, sep="\n")