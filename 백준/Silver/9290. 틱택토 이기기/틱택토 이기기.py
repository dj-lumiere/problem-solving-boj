from itertools import combinations
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
    t = int(input())
    answers = []
    for hh in range(t):
        s1 = input()
        s2 = input()
        s3 = input()
        mark = input()
        board = [list(s1), list(s2), list(s3)]
        answer = ""
        for i in range(3):
            for j in range(3):
                if board[i][j] == '-':
                    board[i][j] = mark
                    win = False
                    if all(board[i][k] == mark for k in range(3)):
                        win = True
                    if all(board[k][j] == mark for k in range(3)):
                        win = True
                    if i == j and all(board[k][k] == mark for k in range(3)):
                        win = True
                    if i + j == 2 and all(board[k][2 - k] == mark for k in range(3)):
                        win = True
                    if win:
                        answer = f"Case {hh+1}:\n{''.join(board[0])}\n{''.join(board[1])}\n{''.join(board[2])}"
                        break
                    board[i][j] = '-'
            if answer:
                break
        answers.append(f"{answer}")
    print(*answers, sep="\n")