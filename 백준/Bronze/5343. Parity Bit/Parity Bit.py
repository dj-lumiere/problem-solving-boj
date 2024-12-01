from sys import stderr, stdout

with open(0, "r", encoding="UTF-8") as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    INF = 10 ** 18
    t = int(input())
    answers = []
    for hh in range(t):
        data = input()
        error_count = 0
        for i in range(0, len(data), 8):
            segment = data[i:i + 8]
            data_bits = segment[:7]
            parity_bit = segment[7]
            count_ones = data_bits.count('1')
            expected_parity = '1' if count_ones % 2 == 1 else '0'
            if parity_bit != expected_parity:
                error_count += 1
        answer = f"{error_count}"
        answers.append(f"{answer}")
    print(*answers, sep="\n")