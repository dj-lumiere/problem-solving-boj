from sys import setrecursionlimit, stdout, stderr

with open(0, 'r') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens, None)
    print = lambda *args, sep="\n", end="\n": stdout.write(sep.join(map(str, args)) + end)
    eprint = lambda *args, sep=" ", end="\n": stderr.write(sep.join(map(str, args)) + end)
    fprint = lambda *args, sep=" ", end="\n", file: file.write(sep.join(map(str, args)) + end)
    is_inbound = lambda pos_x, size_x, pos_y, size_y: 0 <= pos_x < size_x and 0 <= pos_y < size_y
    DELTA = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    INF = 10 ** 18
    MOD = 1_000_000_000
    t = 1
    answers = []
    for hh in range(t):
        n = int(input())
        answer = 0
        if n == 1:
            answer = 1
        elif n < 4:
            answer = 0
        else:
            # col number, row check, diag_ld_check, diag_rd_check
            stack = [(0, 0, 0, 0)]
            while stack:
                col, row_check, diag_ld_check, diag_rd_check = stack.pop()
                if col == n:
                    answer += 1
                    continue
                row = 0
                while row < n:
                    diag_ld = col - row + n - 1
                    diag_rd = col + row
                    if row_check & (1 << row) or diag_ld_check & (1 << diag_ld) or diag_rd_check & (1 << diag_rd):
                        row += 1
                        continue
                    row_check ^= (1 << row)
                    diag_ld_check ^= (1 << diag_ld)
                    diag_rd_check ^= (1 << diag_rd)
                    stack.append((col + 1, row_check, diag_ld_check, diag_rd_check))
                    row_check ^= (1 << row)
                    diag_ld_check ^= (1 << diag_ld)
                    diag_rd_check ^= (1 << diag_rd)
                    row += 1
        answers.append(f"{answer}")
    print(*answers, sep="\n")
