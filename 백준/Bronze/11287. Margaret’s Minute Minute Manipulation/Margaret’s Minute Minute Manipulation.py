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
        T = [[input() for _ in range(6)] for _ in range(4)]
        D = [[input() for _ in range(6)] for _ in range(4)]


        def parse_time(matrix):
            digits = []
            for col in range(6):
                bits = ''.join(matrix[row][col] for row in range(4))
                digits.append(int(bits, 2))
            return digits


        T_digits = parse_time(T)
        D_digits = parse_time(D)
        T_seconds = T_digits[0] * 10 * 3600 + T_digits[1] * 3600 + T_digits[2] * 10 * 60 + T_digits[3] * 60 + T_digits[
            4] * 10 + T_digits[5]
        D_seconds = D_digits[0] * 10 * 3600 + D_digits[1] * 3600 + D_digits[2] * 10 * 60 + D_digits[3] * 60 + D_digits[
            4] * 10 + D_digits[5]
        total_seconds = (T_seconds + D_seconds) % 86400
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        result_digits = [h // 10, h % 10, m // 10, m % 10, s // 10, s % 10]
        matrix = ['' for _ in range(4)]
        for bit in range(3, -1, -1):
            row = ' '.join(['1' if (digit >> bit) & 1 else '0' for digit in result_digits])
            matrix[3 - bit] = row
        answer = '\n'.join(matrix)
        answers.append(f"{answer}")
    print(*answers, sep="\n")