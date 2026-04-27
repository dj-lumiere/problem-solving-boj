import os
from bisect import bisect_left

# with open(0, 'rb') as f:
with open(0, 'rb') as f:
    tokens = iter(f.read().split())
    input = lambda: next(tokens)
    print = lambda x: os.write(1, "\n".join(x).encode())
    eprint = lambda x: os.write(2, (str(x) + "\n").encode())
    t = int(input())
    answers = ["" for _ in range(t)]
    for i in range(t):
        grid = [[int(input()) for _ in range(9)] for _ in range(9)]
        row = [[0 for _ in range(9)] for _ in range(9)]
        col = [[0 for _ in range(9)] for _ in range(9)]
        square = [[0 for _ in range(9)] for _ in range(9)]
        for j in range(9):
            for k in range(9):
                row_num = j
                col_num = k
                square_num = (j // 3) * 3 + k // 3
                item = grid[j][k] - 1
                row[row_num][item] += 1
                col[col_num][item] += 1
                square[square_num][item] += 1
        row += col
        row += square
        answer = "CORRECT" if all(i == [1] * 9 for i in row) else "INCORRECT"
        answers[i] = f"Case {i + 1}: {answer}"
    # while True:
    #     n = int(input())
    #     if n == 0:
    #         break
    #     a = [int(input()) for _ in range(n)]
    #     answers.append("\n".join(map(str, reversed(a)))+"\n0")
    print(answers)